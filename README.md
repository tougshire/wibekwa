# Wibekwa

Wibekwa is a blog app for Wagtail

## Installation

Wibekwa requires wibekwa_base, touglates and wagtail_modeladmin. If you're using a different template app than wibekwa_base, you can substitute that app

These instructions are written with the assumption that you're starting a new project

* create a new Wagtail project (see [Wagtail's instructions](https://docs.wagtail.org/en/v6.2.1/getting_started/) )
* pip install [wagtail-markdown](https://pypi.org/project/wagtail-markdown/)
* pip install [wagtail_modeladmin](https://pypi.org/project/wagtail-modeladmin/)
* git clone [https://github.com/tougshire/touglates](https://github.com/tougshire/touglates)
* git clone [https://github.com/tougshire/wibekwa_base](https://github.com/tougshire/wibekwa_base)
* git clone [https://github.com/tougshire/wibekwa](https://github.com/tougshire/wibekwa)
* add the following to INSTALLED_APPS:
    * "wagtail.contrib.settings"
	* "wagtail_modeladmin"
    * "wagtailmarkdown"
    * "wagtail.contrib.table_block",
	* "touglates"
	* "wibekwa_base"
	* "wibekwa"
* Add the following to your settings:
```
WAGTAILMARKDOWN = {
    "autodownload_fontawesome": True,
    "extensions": ['extra'],
}
```
* run the migrations again
* run collectstatic


## Setting Up

### Wibekwa provides the ability to have a landing page other than the root page.  Webekwa also provides for a static tags index page, where you designate the included tags in the admin panel (aka a "featured" tag or to make use of hidden tags described below, "_personal", "_coding" etc).  The following instructions are a way to make use of those features

* run the server (python manage.py runserver) and browse to the admin panel (127.0.0.1:8000/admin
* rename the automatically-created page
    * in the admin panel, click "Pages", then the edit icon (a pencil) for the automatically created page (which may be "home" or "welcome or something like that)
    * change the title to "Home-Old".  In the promote tab, rename the slug from "home" to "home-old".
    * publish the page
* create a new article index page
    * using the "add child page" action next to the word "Root", create a new article index page
    * name it "Articles"
    * publish the page
* create a new article static tags index page
    * from the root page, create a new article static tags index page
    * name it "Featured Articles"
    * under "tags included" enter "_f1,_f2"
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
	* Click "Yes, move these pages"
* make Home the root page for the default site
    * click "Settings" then "Sites"
    * edit the default site, probably "localhost" unless you changed it, and change the root page from the old home page to the new home page (which is the redirect page)
	* public the change
* You can now add new articles with the "Articles" menu item.  If you tag the article with "_f1" or "_f2", it will show up on your home page under Featured Articles
    * The underscores make the tags hidden so they won't be shown in the tag cloud.  This allows you to use tags for placement on pages without cluttering up the list of tags that are displayed with the article. You can add other tags to an article such as "python" or "wagtail", and those tags will be visible in the list of tags

