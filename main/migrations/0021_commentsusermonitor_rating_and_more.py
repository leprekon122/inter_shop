# Generated by Django 4.0.4 on 2022-05-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_commentsusers_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsusermonitor',
            name='rating',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='commentsusersvideocard',
            name='rating',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=15, null=True),
        ),
    ]
