# Generated by Django 4.0.4 on 2022-05-26 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_questionusersvideocard_link_video_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebookslist',
            name='pic_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='videocards',
            name='pic_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
