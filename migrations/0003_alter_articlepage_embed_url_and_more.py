# Generated by Django 5.0.9 on 2024-09-25 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibekwa', '0002_freearticlepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='embed_url',
            field=models.URLField(blank=True, help_text='For pages with an iFrame, the URL of the embedded contnet', max_length=765, verbose_name='Embed Target URL'),
        ),
        migrations.AlterField(
            model_name='freearticlepage',
            name='embed_url',
            field=models.URLField(blank=True, help_text='For pages with an iFrame, the URL of the embedded contnet', max_length=765, verbose_name='Embed Target URL'),
        ),
        migrations.AlterField(
            model_name='sidebararticlepage',
            name='embed_url',
            field=models.URLField(blank=True, help_text='For pages with an iFrame, the URL of the embedded contnet', max_length=765, verbose_name='Embed Target URL'),
        ),
    ]