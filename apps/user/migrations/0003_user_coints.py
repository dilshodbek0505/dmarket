# Generated by Django 5.1.3 on 2024-11-09 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_managers_remove_user_date_joined_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='coints',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Coins'),
        ),
    ]
