# Wibekwa

Wibekwa is a blog app for Wagtail, modified from the Wagtail tutorial

## Installation

Wibekwa requires wibekwa_base, touglates and wagtail_modeladmin.  Touglates requires markdown. If you're using a different template app than wibekwa_base, you can substitute that app

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
* add "touglates", "wibekwa_base", and "wibekwa" to INSTALLED_APPS in settings/base.py
* add "touglates.context_processors.base_context_settings" to the list of context_processors under TEMPLATES in settings/base.py
* add the following in settings/base.py:
    * you can also write your own template base app and use that instead of wibekwa_base

            BASE_CONTEXT_SETTINGS = {
                'base_html':"base.html",
                'wibekwa_base': 'wibekwa_base',
            }

* run the migrations again

## Usage

### Wibekwa provides the ability to have a landing page other than the root page.  Webekwa also provides for a static tags index page, where you designate the included tags in the admin panel.  The following instructions are a way to make use of those features

* In the admin panel, change the home page name from "Home" to "Z Home" and the slug from "home" to "z-home"
* from the root page, (http://127.0.0.1:8000/admin/pages/ if your site is http://127.0.0.1:8000), create a new blog index page
    * name it "blog"
    * check the "for site menus" check box under the Promote tab
* from the root page, create a new static tags index page
    * name it "featured articles"
    * under "tags included" enter "featured"
* from the root page, create a new redirect page
    * name it "Home"
    * for the target page, choose the featured articles page
* go to http://127.0.0.1:8000/admin/sites (subbing whatever your actual base url is)
* edit localhost and change the root page from Z_Home to Home
* go back to http://127.0.0.1:8000/admin/pages/ and move the featured articles page and the blog page under home
    * Do this by selecting the three dots, then "move", then the three dots, then "choose a different page"
* You can now add new articles with the "Blog Pages" menu item.  If you tag the article with "featured", it will show up on your home page
