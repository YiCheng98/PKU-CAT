# Generated by Django 3.0.5 on 2020-04-13 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200412_2235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterModelOptions(
            name='verification',
            options={'verbose_name': '验证码', 'verbose_name_plural': '验证码'},
        ),
    ]
