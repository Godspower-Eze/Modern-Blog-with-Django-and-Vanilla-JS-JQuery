# Generated by Django 3.1.2 on 2020-10-17 04:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='body',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
