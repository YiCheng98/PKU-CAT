# Generated by Django 3.0.5 on 2020-05-29 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('introduction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('avatar', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(max_length=100)),
                ('archive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Archive')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Cat')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.URLField()),
                ('containing_archive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Archive')),
            ],
        ),
        migrations.AddField(
            model_name='archive',
            name='relatedCats',
            field=models.ManyToManyField(related_name='archive_this_cat_related_to', through='archive.Relationship', to='archive.Cat'),
        ),
    ]
