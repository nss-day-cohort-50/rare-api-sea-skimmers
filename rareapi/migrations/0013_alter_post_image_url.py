# Generated by Django 3.2.9 on 2021-11-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0012_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.URLField(),
        ),
    ]
