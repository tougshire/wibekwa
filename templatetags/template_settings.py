from django import template

from wagtail.models import Site

from wibekwa.models import SiteTemplateSettings

register = template.Library()

@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page

@register.simple_tag(takes_context=True)
def get_template_settings(context):
    template_settings = context.get("template_settings", "")

    template_settings_keys = {
            "header_style",
            "banner_image",
            "show_banner_image",
            "banner_image_style",
            "banner_text",
            "site_description",
            "show_leftbar",
            "show_rightbar",
            "mainmenu_location",
            "theme_color",
            "footer_text",
            "footer_text_separator",
            "favicon",
    }
    if not template_settings:
        template_settings = {}

        instance = SiteTemplateSettings.objects.filter(site=Site.find_for_request(context["request"])).first()
        if not instance:
            instance = SiteTemplateSettings.objects.filter(site=None).first()

        if instance:
            for key in template_settings_keys:
                template_settings[key] = getattr(instance, key)

        else:
            for key in template_settings_keys:
                template_settings[key] = SiteTemplateSettings._meta.get_field(key).default

        if template_settings["footer_text_separator"] and template_settings["footer_text"]:
            template_settings["footer_text"] = template_settings["footer_text"].split(template_settings["footer_text_separator"])

        if not ';' in template_settings["banner_image_style"]:
            template_settings["banner_image_width"] = template_settings["banner_image_style"]
            template_settings["banner_image_style"] = ""


        return template_settings


