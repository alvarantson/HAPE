# Generated by Django 3.0.2 on 2020-09-21 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999)),
                ('url', models.CharField(max_length=999)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=999)),
                ('url', models.CharField(blank=True, max_length=999)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrape.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='Video_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(blank=True)),
                ('likes', models.IntegerField(blank=True)),
                ('dislikes', models.IntegerField(blank=True)),
                ('comments', models.IntegerField(blank=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrape.Video')),
            ],
        ),
    ]
