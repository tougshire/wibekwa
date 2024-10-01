# Generated by Django 5.0.9 on 2024-09-30 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibekwa', '0010_articlepage_show_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlestatictagsindexpage',
            name='show_body_in_index',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'first group'), (9, 'all articles')], default=0, verbose_name='show body instead of summary'),
        ),
    ]
