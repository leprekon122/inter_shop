# Generated by Django 4.0.4 on 2022-05-29 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_questionusersmonitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsusers',
            name='rating',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=15, null=True),
        ),
    ]
