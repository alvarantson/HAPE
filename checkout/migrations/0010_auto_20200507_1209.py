# Generated by Django 2.2.7 on 2020-05-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20200501_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy_history',
            name='receipt',
            field=models.TextField(),
        ),
    ]
