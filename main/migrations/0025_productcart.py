# Generated by Django 4.0.4 on 2022-06-05 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0024_alter_commentsusermemory_name_of_stuff_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=255)),
                ('product_pic', models.ImageField(upload_to='ProductCartPic')),
                ('product_price', models.IntegerField()),
                ('product_status', models.CharField(choices=[('Є в наявності', 'Є в наявності'), ('Немає в наявності', 'Немає в наявності')], max_length=255)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ProductCart',
                'verbose_name_plural': 'ProductsCart',
            },
        ),
    ]
