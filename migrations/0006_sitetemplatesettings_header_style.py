# Generated by Django 5.0.9 on 2024-09-26 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibekwa', '0005_delete_articletagindexpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitetemplatesettings',
            name='header_style',
            field=models.CharField(blank=True, default='50%', help_text='Inline styling for the header', max_length=255),
        ),
    ]