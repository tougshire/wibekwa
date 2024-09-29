# Generated by Django 5.0.9 on 2024-09-27 00:54

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wibekwa', '0006_sitetemplatesettings_header_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='body_sf',
            field=wagtail.fields.StreamField([('heading_block', 2), ('paragraph_block', 3), ('image_block', 7), ('embed_block', 8)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a heading size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], 'required': False}), 2: ('wagtail.blocks.StructBlock', [[('heading_text', 0), ('size', 1)]], {}), 3: ('wagtail.blocks.RichTextBlock', (), {'icon': 'pilcrow'}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.CharBlock', (), {'required': True}), 7: ('wagtail.blocks.StructBlock', [[('image', 4), ('caption', 5), ('attribution', 5), ('alt', 6)]], {}), 8: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks', 'icon': 'media'})}),
        ),
    ]
