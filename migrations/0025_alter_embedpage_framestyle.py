# Generated by Django 5.0.9 on 2024-09-24 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibekwa', '0024_embedpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embedpage',
            name='framestyle',
            field=models.CharField(blank=True, default='width:100%; height:1200px;', help_text='Styling for the frame', max_length=255, verbose_name='Frame Style'),
        ),
    ]
