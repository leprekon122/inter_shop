# Generated by Django 4.0.4 on 2022-05-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_commentsusers_delete_commentsuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsusers',
            name='name_of_user',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
