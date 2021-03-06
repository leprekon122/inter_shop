# Generated by Django 4.0.4 on 2022-05-28 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_commentsusermonitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionUsersMonitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_user', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('name_of_stuff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.monitors_list')),
            ],
            options={
                'verbose_name': 'QuestionUsersMonitor',
                'verbose_name_plural': "QuestionUsersMonitor's",
            },
        ),
    ]
