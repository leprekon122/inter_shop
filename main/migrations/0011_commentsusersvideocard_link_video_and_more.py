# Generated by Django 4.0.4 on 2022-05-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_questionusersvideocard_commentsusersvideocard'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsusersvideocard',
            name='link_video',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='questionusersvideocard',
            name='link_video',
            field=models.TextField(blank=True, null=True),
        ),
    ]
