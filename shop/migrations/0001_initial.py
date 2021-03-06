# Generated by Django 3.0.2 on 2020-08-25 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999, unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField()),
                ('discount_percentage', models.PositiveIntegerField(default=0)),
                ('img', models.ImageField(upload_to='')),
                ('img_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('img_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('img_4', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
