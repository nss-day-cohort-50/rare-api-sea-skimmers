# Generated by Django 3.2.9 on 2021-11-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0007_alter_author_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
