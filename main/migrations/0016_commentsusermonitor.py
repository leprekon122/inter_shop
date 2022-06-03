# Generated by Django 4.0.4 on 2022-05-28 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_monitors_monitors_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsUserMonitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_user', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('link_video', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('name_of_stuff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.monitors_list')),
            ],
            options={
                'verbose_name': 'CommentsUserMonitor',
                'verbose_name_plural': 'CommentsUserMonitors',
            },
        ),
    ]
