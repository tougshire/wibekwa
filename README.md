# Wibekwa

Wibekwa is a blog app for Wagtail, modified from the Wagtail tutorial

## Installation

Wibekwa requires Wibekwa_base, Touglates and Wagtail ModelAdmin.  Touglates requires Markdown.

These instructions are written with the assumption that you're starting a new project

* create a Wagtail project in accordance with [Wagtail's instructions](https://docs.wagtail.org/en/v6.2.1/getting_started/)
    * note: regarding Django projects in general, if you want to add a [custom user model](https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project), it's best to do so before your first migration. If you do, put your AUTH_USER_MODEL and related parameters in settings/base.py
    * You can stop at the part about creating the basic blog, but if you're not familiar with Wagtail, continue with the tutorial. If you do, you should delete the blog folder and remove "blog" from installed apps before continuing with these instructions.
* pip install [markdown](https://pypi.org/project/Markdown/)
* pip install [wagtail_modeladmin](https://pypi.org/project/wagtail-modeladmin/)
* git clone [https://github.com/tougshire/touglates](https://github.com/tougshire/touglates)
* git clone [https://github.com/tougshire/wibekwa_base](https://github.com/tougshire/wibekwa_base)
* git clone [https://github.com/tougshire/wibekwa](https://github.com/tougshire/wibekwa)
* add "wagtail.contrib.settings" and "wagtail_modeladmin" to your installed apps (for neatness, add them below "wagtail.admin")
* add "touglates" and "wibekwa" to your installed apps
* add "touglates.context_processors.base_context_settings" to the list of context_processors under TEMPLATES in base.py
* add the following in base.py:
    * you can also write your own template base app and use that instead of wibekwa_base

            BASE_CONTEXT_SETTINGS = {
                'base_html':"base.html",
                'wibekwa_base': 'wibekwa_base',
            }

* run the migrations again
* Continue with the tutorial at the section Blog index and posts





