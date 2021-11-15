# Generated by Django 3.2.9 on 2021-11-15 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0003_alter_comment_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='follower',
        ),
        migrations.AddField(
            model_name='subscription',
            name='follower',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='following', to='rareapi.author'),
            preserve_default=False,
        ),
    ]