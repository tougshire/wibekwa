# Generated by Django 5.0.9 on 2024-11-29 23:19

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
        ('wibekwa', '0016_alter_articlepage_body_sf_alter_freearticlepage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCommentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Post date')),
                ('body', models.CharField(blank=True, help_text='The body of the comment', max_length=250)),
                ('commenter_display_name', models.CharField(blank=True, help_text='The body of the comment', max_length=250)),
                ('in_reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wibekwa.articlecommentpage')),
            ],
            options={
                'verbose_name': 'Comment',
            },
            bases=('wagtailcore.page',),
        ),
    ]
