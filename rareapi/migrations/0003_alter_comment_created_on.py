# Generated by Django 3.2.9 on 2021-11-15 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0002_alter_author_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateField(),
        ),
    ]