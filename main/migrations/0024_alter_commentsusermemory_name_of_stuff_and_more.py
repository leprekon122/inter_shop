# Generated by Django 4.0.4 on 2022-06-02 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_memory_list_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsusermemory',
            name='name_of_stuff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.memory_list'),
        ),
        migrations.AlterField(
            model_name='questionusersmemory',
            name='name_of_stuff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.memory_list'),
        ),
    ]
