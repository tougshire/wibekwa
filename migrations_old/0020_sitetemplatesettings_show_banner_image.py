# Generated by Django 5.0.9 on 2024-09-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibekwa', '0019_sitetemplatesettings_banner_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitetemplatesettings',
            name='show_banner_image',
            field=models.BooleanField(default=True, help_text='Show the chosen banner image.  If deselected, banner_text will be used instead of the image', verbose_name='show banner image'),
        ),
    ]
