# Generated by Django 5.0.9 on 2024-09-22 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibekwa', '0011_articlestatictagsindexpage_first_group_is_special'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_leftbar', models.BooleanField(default=False, help_text='If the left sidebar should be shown - requires a template named wibewa/includes/sidebarleft.html')),
                ('show_rightbar', models.BooleanField(default=False, help_text='If the right sidebar should be shown - requires a template named wibewa/includes/sidebarright.html')),
                ('mainmenu_location', models.CharField(choices=[('none', 'None'), ('top', 'Top'), ('left', 'Left'), ('right', 'Right')], default='top', help_text='The location of the main menu', max_length=20, verbose_name='main menu location')),
                ('theme_color', models.CharField(default='blue', help_text='The theme color. This should match the base name of a css file in a static folder wibekwa/css', max_length=30, verbose_name='theme color')),
            ],
            options={
                'verbose_name_plural': 'Template Settings',
            },
        ),
    ]