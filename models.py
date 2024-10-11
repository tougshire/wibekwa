import datetime
import re
from django import forms
from django.db import models
from django.conf import settings
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,

)

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel

from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)

from wagtail.fields import StreamField, RichTextField
from wagtail.documents import get_document_model

from wagtail.models import Page, Orderable

from wagtail.search import index
from wagtail.snippets.models import register_snippet

from .blocks import BodyStreamBlock

def get_sidebars(request):
    sidebars = []
    for sidebarpage in SidebarPage.objects.live().all():
        sidebar = {"location":sidebarpage.location, "children":[]}
        for childpage in sidebarpage.get_children():
            child={"title":childpage.title, "body":childpage.specific.body, "context": childpage.specific.get_context(request)}
            sidebar["children"].append(child)
        sidebars.append(sidebar)
    return sidebars




class RedirectPage(Page):

    target_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        PageChooserPanel('target_page'),
    ]

    def route(self, request, path_components):
        if path_components:
            return super().route(request, path_components)
        else:
            path_components=[self.target_page.slug]
            return super().route(request, path_components)

class ArticleIndexPage(Page):
    intro = RichTextField(blank=True)
    show_pagetitle=models.BooleanField( default=True, help_text="If the page title should be shown" )

    content_panels = Page.content_panels + [
        FieldPanel('show_pagetitle'),
        FieldPanel('intro')
    ]

    def get_context(self, request):

        tag = request.GET.get('tag')

        context = super().get_context(request)
        ArticlePages = self.get_children().live().order_by('-first_published_at')
        if tag:
            ArticlePages = ArticlePage.objects.filter(tags__name=tag)
        for article_page in ArticlePages:
            print('tp249q729', article_page)

        context['articlepages'] = ArticlePages

        context['sidebars'] = get_sidebars(request)

        return context

class SidebarPage(Page):
    intro = RichTextField(blank=True)
    show_pagetitle=models.BooleanField( default=True, help_text="If the page title should be shown" )
    location = models.CharField("location", max_length=40, blank=True, choices=(("left","left"),("right","right"),("top","top"),("bottom","bottom")))

    content_panels = Page.content_panels + [
        FieldPanel('show_pagetitle'),
        FieldPanel('intro'),
        FieldPanel('location')
    ]

    def get_context(self, request):
        context = super().get_context(request)
        ArticlePages = self.get_children().live().order_by('-first_published_at')
        context['articlepages'] = ArticlePages
        return context

@register_snippet
class ArticlePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ArticlePage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class ArticlePage(Page):
    date = models.DateField("Post date", default=datetime.date.today)
    summary = models.CharField(max_length=250, blank=True, help_text='A summary to be displayed instead of the body for index views')
    body_sf = StreamField(BodyStreamBlock(), blank=True, use_json_field=True)
    embed_url = models.URLField("Embed Target URL", max_length=765, blank=True, help_text="For pages with an iFrame, the URL of the embedded contnet")
    embed_frame_style = models.CharField("Frame Style", max_length=255, blank=True, default="width:90%; height:1600px;", help_text="For pages with an iFrame, styling for the frame")
    document = models.ForeignKey(get_document_model(), null=True,blank=True,on_delete=models.SET_NULL,)
    show_doc_link = models.BooleanField("show doc link", default=True, help_text="Show the document link automatically.  One reason to set false would be you're already placing a link in the body")
    show_gallery = models.BooleanField("show doc link", default=True, help_text="Show the gallery")
    authors = ParentalManyToManyField('wibekwa.Author', blank=True)
    tags = ClusterTaggableManager(through=ArticlePageTag, blank=True)

    parent_page_types = ["ArticleIndexPage"]

    def get_context(self, request):
        context=super().get_context(request)
        context['visible_tags']=[]
        for tag in context['page'].tags.all():

            if not tag.name[0] == '_':
                context['visible_tags'].append(tag)

        # restrict allowable embeds by listing them in settings.  "https://tougshire.com/12345" will match if "https://tougshire.com" is listed
        allow_embed = False
        if self.embed_url:
            if hasattr(settings,"ALLOWED_EMBED_URLS"):
                for allowed_url in settings.ALLOWED_EMBED_URLS:
                    if allowed_url in self.embed_url[0:len(allowed_url)]:
                        allow_embed = True
            else:
                allow_embed = True

            if allow_embed:
                context['embed_url'] = self.embed_url
                context['embed_frame_style'] = self.embed_frame_style

        context['sidebars'] = get_sidebars(request)

        return context


    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('summary'),
        index.SearchField('body_sf'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('date'),
                FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
                FieldPanel('tags'),
            ],
            heading="Article information"
        ),
        FieldPanel('summary'),
        FieldPanel('body_sf'),
        MultiFieldPanel(
            [
                FieldPanel('document'),
                FieldPanel('show_doc_link'),
            ],
            heading="Document"
        ),
        MultiFieldPanel(
            [
                InlinePanel('gallery_images', label="Gallery images"),
                FieldPanel('show_gallery'),
            ]
        ),
        MultiFieldPanel(
            [
                FieldPanel('embed_url'),
                FieldPanel('embed_frame_style'),
            ],
            heading="Embedded Content"
        ),

    ]

class FreeArticlePage(Page):

    body = StreamField(BodyStreamBlock(), blank=True, use_json_field=True)
    embed_url = models.URLField("Embed Target URL", blank=True, max_length=765, help_text="For pages with an iFrame, the URL of the embedded contnet")
    embed_frame_style = models.CharField("Frame Style", max_length=255, blank=True, default="width:90%; height:1600px;", help_text="For pages with an iFrame, styling for the frame")

    def get_context(self, request):
        context=super().get_context(request)

        # restrict allowable embeds by listing them in settings.  "https://tougshire.com/12345" will match if "https://tougshire.com" is listed
        allow_embed = False
        if self.embed_url:
            if hasattr(settings,"ALLOWED_EMBED_URLS"):
                for allowed_url in settings.ALLOWED_EMBED_URLS:
                    if allowed_url in self.embed_url[0:len(allowed_url)]:
                        allow_embed = True
            else:
                allow_embed = True

            if allow_embed:
                context['embed_url'] = self.embed_url
                context['embed_frame_style'] = self.embed_frame_style

        context['sidebars'] = get_sidebars[request]

        return context


        return context


    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [

        FieldPanel('body'),
        MultiFieldPanel(
            [
                FieldPanel('embed_url'),
                FieldPanel('embed_frame_style'),
            ],
            heading="Embedded Content"
        ),

    ]


class SidebarArticlePage(Page):

    body = RichTextField(blank=True,)
    embed_url = models.URLField("embed target URL", blank=True, max_length=765, help_text="For pages with an iFrame, the URL of the embedded contnet")
    embed_frame_style = models.CharField("frame style", max_length=255, blank=True, default="width:90%; height:1600px;", help_text="For pages with an iFrame, styling for the frame")
    parent_page_types = ["SidebarPage"]

    def get_context(self, request):
        context=super().get_context(request)

        # restrict allowable embeds by listing them in settings.  "https://tougshire.com/12345" will match if "https://tougshire.com" is listed
        allow_embed = False
        if self.embed_url:
            if hasattr(settings,"ALLOWED_EMBED_URLS"):
                for allowed_url in settings.ALLOWED_EMBED_URLS:
                    if allowed_url in self.embed_url[0:len(allowed_url)]:
                        allow_embed = True
            else:
                allow_embed = True

            if allow_embed:
                context['embed_url'] = self.embed_url
                context['embed_frame_style'] = self.embed_frame_style

        return context

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [

        FieldPanel('body'),
        MultiFieldPanel(
            [
                FieldPanel('embed_url'),
                FieldPanel('embed_frame_style'),
            ],
            heading="Embedded Content"
        ),

    ]


class ArticlePageGalleryImage(Orderable):
    page = ParentalKey(
        ArticlePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    author_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('author_image'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'

# class ArticleTagIndexPage(Page):

#     def get_context(self, request):

#         tag = request.GET.get('tag')
#         ArticlePages = ArticlePage.objects.live().filter(tags__name=tag)

#         context = super().get_context(request)
#         context['ArticlePages'] = ArticlePages
#         return context

class ArticleStaticTagsIndexPage(Page):

    show_pagetitle=models.BooleanField( default=True, help_text="If the page title should be shown" )
    included_tag_names_string = models.CharField("tags included", max_length=255, blank=True, help_text="A comma separated list of tags to be included in this page which can also be grouped - separate groups with semicolon")
    tag_titles_string = models.CharField("tag titles", max_length=255, blank=True, help_text="A comma separated list of titles to be used instead of the tag names - not separated by group")
    group_titles_string = models.CharField("group titles", max_length=255, blank=True, help_text="A comma separated list of titles to be used for tag groups")
    apply_special_formatting = models.IntegerField("apply special formatting", default=False, help_text="The group number up to which special formatting should be applied.  Implementation may vary by template app")
    show_body_in_index = models.IntegerField("show body instead of summary", default=0, help_text="The group number up to which articles will show the entire body instead of the summary")
    separate_tag_groups = models.BooleanField(default=True, help_text="If the ArticlePages should be separated by tag")
    show_tag_titles = models.BooleanField(default=True, help_text='If the tag name should be displayed as a title to accompany the ArticlePages')

    content_panels = Page.content_panels + [


        FieldPanel('show_pagetitle'),
        MultiFieldPanel(
            [
                FieldPanel('included_tag_names_string'),
                MultiFieldPanel([
                    FieldPanel('tag_titles_string'),
                    FieldPanel('group_titles_string'),
                    FieldPanel('separate_tag_groups'),
                ], heading="Tag Titles"),
                FieldPanel('show_tag_titles'),
                MultiFieldPanel([
                    FieldPanel('show_body_in_index'),
                    FieldPanel('apply_special_formatting'),
                ],heading="First Groups")
            ]
        )
    ]

    def get_context(self, request):

        context = super().get_context(request)

        article_page_groups = []

        included_tag_name_groups = self.included_tag_names_string.split(';')
        tag_titles = re.split(r';|,', self.tag_titles_string ) if self.tag_titles_string > '' else []
        group_titles = re.split(r';|,', self.group_titles_string ) if self.group_titles_string > '' else []

        t = 0
        for g in range(len(included_tag_name_groups)):
            new_article_page_group = {'article_page_sets':[]}
            if len(group_titles) > g:
                if group_titles[g] > '':
                    new_article_page_group['group_title'] = group_titles[g]
            article_page_sets = []
            included_tag_names = included_tag_name_groups[g].split(',')

            for i in range(len(included_tag_names)):
                included_tag_name = included_tag_names[i].strip()
                new_article_page_set={}

                new_article_page_set['article_pages'] = ArticlePage.objects.live().filter(tags__name=included_tag_name).order_by('-latest_revision_created_at')

                if new_article_page_set['article_pages']:
                    new_article_page_set['tagname'] = included_tag_name
                    tag_title = tag_titles[t].strip() if len(tag_titles ) > t else included_tag_name
                    new_article_page_set['title'] = tag_title
                    article_page_sets.append(new_article_page_set)

                t = t + 1


            if article_page_sets:
                new_article_page_group['article_page_sets']=article_page_sets

                article_page_groups.append(new_article_page_group)


        context['sidebars'] = get_sidebars(request)

        context['article_page_groups'] = article_page_groups
        # context['first_group_is_special'] = self.first_group_is_special

        return context

@register_setting
class SiteSpecificImportantPages(BaseSiteSetting):
    article_index_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('article_index_page'),
    ]

@register_setting
class SiteTemplateSettings(BaseSiteSetting):

    header_style = models.CharField(
        max_length=255,
        blank=True,
        default="50%",
        help_text="Inline styling for the header",
    )

    banner_image = models.ForeignKey(
        'wagtailimages.Image', related_name='+',
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL
    )
    show_banner_image = models.BooleanField(
        'show banner image',
        default=True,
        help_text="Show the chosen banner image.  If deselected, banner_text will be used instead of the image"
    )
    banner_image_style = models.CharField(
        max_length=255,
        blank=True,
        default="50%",
        help_text="Styling for the banner image or if a single value, A css value representing the width of the banner image. Include at least one semicolon (;) to indicate that this is a style, and not just a width value"
    )
    banner_text = models.CharField(
        "banner_text",
        max_length=80,
        blank=True,
        default="Wibekwa",
        help_text="The alt text to be displayed if there is a banner image, or the text to be displayed if there is no image"
    )
    site_description=models.CharField(
        "site description",
        max_length=80,
        blank=True,
        default="New Wibewa Wagtail Blog",
        help_text="The site description to be displayed near the banner image or banner text"
    )
    show_leftbar=models.BooleanField(
        default=False,
        help_text="If the left sidebar should be shown - requires a template named wibewa/includes/sidebarleft.html"
    )
    show_rightbar=models.BooleanField(
        default=False,
        help_text="If the right sidebar should be shown - requires a template named wibewa/includes/sidebarright.html"
    )
    mainmenu_location=models.CharField(
        "main menu location",
        max_length=20,
        choices=(("none","None"),("top","Top"),("left","Left"),("right","Right")),
        help_text="The location of the main menu",
        default="top"
    )
    theme_color=models.CharField(
        "theme color",
        max_length=30,
        default="black",
        help_text='The theme color. This should match the base name of a css file in a static folder wibekwa/css. Ex "blue" if there is a wibekwa/css/blue.css'
    )
    footer_text=models.CharField(
        "footer text",
        max_length=255,
        blank=True,
        default="Created wth Wagtail and Wibekwa",
        help_text="The footer text.  This may be split into a list using footer_text_separator",
    )
    footer_text_separator=models.CharField(
        "footer text separator",
        max_length=2,
        blank=True,
        default=';',
        help_text="The character by which the footer text will be split into a list.  This is optional"
    )

    def __str__(self):
        return "Template Settings for " + self.site.__str__() if self.site is not None else "None"

    class Meta():
        verbose_name_plural = "Template Settings"

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')

class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address'),
                FieldPanel('to_address'),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

