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
* run collectstatic

## Setting Up

### Wibekwa provides the ability to have a landing page other than the root page.  Webekwa also provides for a static tags index page, where you designate the included tags in the admin panel (aka a "featured" tag or to make use of hidden tags described below, "_personal", "_coding" etc).  The following instructions are a way to make use of those features

* rename the automatically-created page
    * in the admin panel, click "Pages", then the edit icon (a pencil) for the automatically created page (which may be "home" or "welcome or something like that)
    * in the promote tab, rename the slug from "home" to "home-old".  If the title is "Home", rename it to "Home-Old"
    * publish the page
* create a new article index page
    * using the "add child page" action next to the word "Root", create a new article index page
    * name it "Articles"
    * publish the page
* create a new article static tags index page
    * from the root page, create a new article static tags index page
    * name it "featured articles"
    * under "tags included" enter "_coding,_personal"
    * publish the page
* create a new redirect page
    * from root, create a new redirect page
    * name it "Home"
    * for the target page, choose the featured articles page
    * publish the page
* move the featured articles page and the articles index page under the home page
    * from the page list under root, check the checkboxes next to Featured Articles and Articles
    * click the "move" button
    * click the three dots next to "Root" and "Choose another page"
    * choose Home
* make Home the root page for the default site
    * click "Settings" then "Sites"
    * edit localhost and change the root page from the old home page to the new home page (which is the redirect page)
* You can now add new articles with the "Blog Pages" menu item.  If you tag the article with "_personal" or "_coding", it will show up on your home page
    * The underscores make the tags hidden so they won't be shown in the tag cloud.  This allows you to use tags for positioning on pages without cluttering up the list of tags that are displayed with the article. You can tag an article with both "_personal" and "personal" to designate a personal post that is on the featured posts page
