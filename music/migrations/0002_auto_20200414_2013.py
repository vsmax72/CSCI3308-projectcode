# Generated by Django 3.0.4 on 2020-04-15 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_downvote',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='song',
            name='is_upvote',
            field=models.BooleanField(default=False),
        ),
    ]
