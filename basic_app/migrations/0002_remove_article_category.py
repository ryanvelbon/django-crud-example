# Generated by Django 2.1.4 on 2018-12-07 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
    ]
