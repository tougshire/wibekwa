# Generated by Django 5.0.9 on 2024-09-17 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
        ('wibekwa', '0004_redirectpage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogTagsIndexPage',
            new_name='BlogStaticTagsIndexPage',
        ),
    ]