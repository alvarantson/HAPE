# Generated by Django 3.0.2 on 2020-08-25 19:53

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='random_str',
            field=models.CharField(default=shop.models.id_generator, max_length=999),
        ),
    ]
