import datetime
import re
from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
)
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)



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
            print('tp202499611', self.target_page.slug)
            path_components=[self.target_page.slug]
            return super().route(request, path_components)

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_context(self, request):
        context = super().get_context(request)
        BlogPages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = BlogPages
        return context

@register_snippet
class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )
    hide_from_lists = models.BooleanField('hide from lists', default=False, help_text="if this tag should be hidden from the list of tags in an BlogPage's meta section and similar locations")

class BlogPage(Page):
    date = models.DateField("Post date", default=datetime.date.today)
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    authors = ParentalManyToManyField('wibekwa.Author', blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    parent_page_types = ['BlogIndexPage']

    def get_context(self, request):
        context=super().get_context(request)
        context['visible_tags']=[]
        for tag in context['page'].tags.all():
            if not tag.name[0] == '_':
                context['visible_tags'].append(tag.name)

        return context


    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('date'),
                FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
                FieldPanel('tags'),
            ],
            heading="Blog information"
        ),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

class NonBlogPage(Page):
    date = models.DateField("Post date", default=datetime.date.today)
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    authors = ParentalManyToManyField('wibekwa.Author', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('date'),
                FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
            ],
            heading="Blog information"
        ),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class NonBlogPageGalleryImage(Orderable):
    page = ParentalKey(NonBlogPage, on_delete=models.CASCADE, related_name='gallery_images')
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

class BlogTagIndexPage(Page):

    def get_context(self, request):

        tag = request.GET.get('tag')
        BlogPages = BlogPage.objects.filter(tags__name=tag)

        context = super().get_context(request)
        context['BlogPages'] = BlogPages
        return context

class BlogTagsIndexPage(Page):

    included_tag_names_string = models.CharField("tags included", max_length=255, blank=True, help_text="A comma separated list of tags to be included in this page which can also be grouped - separate groups with semicolon")
    tag_titles_string = models.CharField("tags titles", max_length=255, blank=True, help_text="A comma separated list of titles to be used instead of the tag names")
    separate_tag_groups = models.BooleanField(default=True, help_text="If the BlogPages should be separated by tag")
    repeat_BlogPages = models.BooleanField(default=True, help_text="If separated by tag, if BlogPages that have multiple included tags should be repeated")
    show_tag_titles = models.BooleanField(default=True, help_text='If the tag name should be displayed as a title to accompany the BlogPages')

    content_panels = Page.content_panels + [
        FieldPanel('included_tag_names_string'),
        MultiFieldPanel(
            [
                FieldPanel('tag_titles_string'),
                FieldPanel('separate_tag_groups'),
                FieldPanel('repeat_BlogPages'),
                FieldPanel('show_tag_titles')
            ]
        )
    ]

    def get_context(self, request):

        blog_page_groups = []

        included_tag_name_groups = self.included_tag_names_string.split(';')
        tag_titles = re.split(r';|,', self.tag_titles_string )

        t = 0
        for g in range(len(included_tag_name_groups)):
            new_blog_page_group = {'page_sets':[]}
            page_sets = []
            included_tag_names = included_tag_name_groups[g].split(',')

            for i in range(len(included_tag_names)):
                included_tag_name = included_tag_names[i].strip()
                new_blog_page_set={}

                new_blog_page_set['pages'] = BlogPage.objects.filter(tags__name=included_tag_name)

                if new_blog_page_set['pages']:
                    new_blog_page_set['tagname'] = included_tag_name
                    tag_title = tag_titles[t].strip() if len(tag_titles ) > t else included_tag_name
                    new_blog_page_set['title'] = tag_title
                    page_sets.append(new_blog_page_set)

                t = t + 1


            if page_sets:
                new_blog_page_group['page_sets']=page_sets

                blog_page_groups.append(new_blog_page_group)




        context = super().get_context(request)
        context['page_groups'] = blog_page_groups
        context['show_tag_titles'] = self.show_tag_titles

        return context

@register_setting
class SiteSpecificImportantPages(BaseSiteSetting):
    blog_index_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('blog_index_page'),
    ]
