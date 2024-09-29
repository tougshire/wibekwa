# Generated by Django 5.0.9 on 2024-09-29 13:21

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wibekwa', '0008_alter_articlepage_body_sf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepage',
            name='body',
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='body_sf',
            field=wagtail.fields.StreamField([('paragraph_block', 0), ('heading_block', 3), ('document_block', 4), ('quote_block', 5), ('image_block', 10), ('embed_block', 11), ('table', 12)], blank=True, block_lookup={0: ('wagtail.blocks.RichTextBlock', (), {'features': ['link', 'bold', 'italic', 'ol', 'ul'], 'icon': 'pilcrow'}), 1: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 2: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a heading size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], 'required': False}), 3: ('wagtail.blocks.StructBlock', [[('heading_text', 1), ('size', 2)]], {}), 4: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 5: ('wagtail.blocks.BlockQuoteBlock', (), {}), 6: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 7: ('wagtail.blocks.CharBlock', (), {'required': False}), 8: ('wagtail.blocks.CharBlock', (), {'required': True}), 9: ('wagtail.blocks.URLBlock', (), {'required': False}), 10: ('wagtail.blocks.StructBlock', [[('image', 6), ('caption', 7), ('attribution', 7), ('alt', 8), ('link', 9)]], {}), 11: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks', 'icon': 'media'}), 12: ('wagtail.contrib.table_block.blocks.TableBlock', (), {})}),
        ),
        migrations.RemoveField(
            model_name='freearticlepage',
            name='body',
        ),
        migrations.AddField(
            model_name='freearticlepage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph_block', 0), ('heading_block', 3), ('document_block', 4), ('quote_block', 5), ('image_block', 10), ('embed_block', 11), ('table', 12)], blank=True, block_lookup={0: ('wagtail.blocks.RichTextBlock', (), {'features': ['link', 'bold', 'italic', 'ol', 'ul'], 'icon': 'pilcrow'}), 1: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 2: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a heading size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], 'required': False}), 3: ('wagtail.blocks.StructBlock', [[('heading_text', 1), ('size', 2)]], {}), 4: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 5: ('wagtail.blocks.BlockQuoteBlock', (), {}), 6: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 7: ('wagtail.blocks.CharBlock', (), {'required': False}), 8: ('wagtail.blocks.CharBlock', (), {'required': True}), 9: ('wagtail.blocks.URLBlock', (), {'required': False}), 10: ('wagtail.blocks.StructBlock', [[('image', 6), ('caption', 7), ('attribution', 7), ('alt', 8), ('link', 9)]], {}), 11: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks', 'icon': 'media'}), 12: ('wagtail.contrib.table_block.blocks.TableBlock', (), {})}),
        ),
    ]