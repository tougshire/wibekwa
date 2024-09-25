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

* run the migrations again

## Usage

### Wibekwa provides the ability to have a landing page other than the root page.  Webekwa also provides for a static tags index page, where you designate the included tags in the admin panel.  The following instructions are a way to make use of those features

* rename the automatically-created page
    * In the admin panel, click "Pages", then the edit icon (a pencil) for "Wecome to your new Wagtail site!"
    * In the promote tab, rename the slug from "home" to "old-home"
    * Publish the page
* using the "add child page" action next to the word "Root", create a new article index page
    * name it "articles"
    * check the "for site menus" check box under the Promote tab
    * Publish the page
* from the root page, create a new article static tags index page
    * name it "featured articles"
    * under "tags included" enter "featured"
    * Publish the page
* from the root page, create a new redirect page
    * name it "Home"
    * for the target page, choose the featured articles page
    * Publish the page
* Move the featured articles page and the articles index page under the home page
    * Do this each page from the page list by selecting the three dots next to the page title, then "move".  After moving each page, get back to the page list by clicking "Pages", then "Pages" next to the home icon
* Click "Settings" then "Sites"
* edit localhost and change the root page from the old home page to the new home page (which is the redirect page)
* You can now add new articles with the "Blog Pages" menu item.  If you tag the article with "featured", it will show up on your home page
