# Generated by Django 5.1.3 on 2024-11-09 06:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_alter_cart_options_alter_cartitem_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Model id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=256, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='Title')),
                ('image', models.ImageField(upload_to='banner_image/', verbose_name='Image for desktop')),
                ('phone_image', models.ImageField(upload_to='banner_image/', verbose_name='Image for phone')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
                'ordering': ('order', '-created_at'),
            },
        ),
    ]
