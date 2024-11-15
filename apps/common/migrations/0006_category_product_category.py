# Generated by Django 5.1.3 on 2024-11-08 14:28

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_productsize_description_productsize_description_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Model id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=128, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=128, null=True, verbose_name='Name')),
                ('cateogry_type', models.CharField(choices=[('food', 'food'), ('fast_food', 'fast_food')], max_length=28, verbose_name='Category type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='common.category', verbose_name='Category'),
        ),
    ]
