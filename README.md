# Wibekwa

Wibekwa is a blog app for Wagtail, modified from the Wagtail tutorial

## Installation

Wibekwa depends on Touglates and Wagtail ModelAdmin.  Touglates requires Markdown

These instructions are written with the assumption that you're starting a new project

* create a Wagtail project in accordance with [Wagtail's instructions](https://docs.wagtail.org/en/v6.2.1/getting_started/)
    * note: regarding Django projects in general, if you want to add a [custom user model](https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project), it's best to do so before your first migration. If you do, put your AUTH_USER_MODEL and related parameters in settings/base.py
    * You can stop at the part about creating the basic blog, but if you're not familiar with Wagtail, continue with the tutorial. If you do, you should delete the blog folder and remove "blog" from installed apps before continuing with these instructions.
* pip install [markdown](https://pypi.org/project/Markdown/)
* pip install [wagtail_modeladmin](https://pypi.org/project/wagtail-modeladmin/)
* git clone [https://github.com/tougshire/touglates](https://github.com/tougshire/touglates)
* git clone [https://github.com/tougshire/wibekwa](https://github.com/tougshire/wibekwa)
* add "wagtail.contrib.settings", to your installed apps (for neatness, add it below "wagtail.admin")
* add "touglates" and "wibekwa" to your installed apps
* run the migrations again
* Continue with the tutorial at the section Blog index and posts





