# Generated by Django 3.0.5 on 2020-04-12 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublisherInfo',
            fields=[
                ('userID', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('avatar', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postID', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('text', models.CharField(max_length=2000)),
                ('isvideo', models.NullBooleanField(default=None)),
                ('video', models.URLField(null=True)),
                ('self_favor', models.BooleanField(default=False)),
                ('favorcnt', models.IntegerField(default=0)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.PublisherInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.URLField()),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentID', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=500)),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.PublisherInfo')),
            ],
        ),
    ]