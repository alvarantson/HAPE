# Generated by Django 3.0.2 on 2020-08-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0002_remove_release_artists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='date',
            field=models.DateField(),
        ),
    ]