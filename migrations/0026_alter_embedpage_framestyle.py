# Generated by Django 5.0.9 on 2024-09-25 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibekwa', '0025_alter_embedpage_framestyle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embedpage',
            name='framestyle',
            field=models.CharField(blank=True, default='width:90%; height:1600px;', help_text='Styling for the frame', max_length=255, verbose_name='Frame Style'),
        ),
    ]