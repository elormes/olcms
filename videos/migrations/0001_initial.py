# Generated by Django 2.0.3 on 2018-03-16 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=5000)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='')),
                ('title', models.CharField(max_length=50)),
                ('views', models.IntegerField(blank=True, default=0)),
                ('description', models.CharField(max_length=5000)),
                ('date_uploaded', models.DateField(auto_now=True)),
                ('likes', models.IntegerField(blank=True, default=0)),
                ('category', models.ManyToManyField(to='videos.Category')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='videos.Playlist')),
                ('tags', models.ManyToManyField(to='videos.Tags')),
            ],
        ),
    ]
