# Generated by Django 2.2.14 on 2020-07-09 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_postmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authormodel',
            name='published_date',
        ),
    ]
