# Generated by Django 2.0.6 on 2018-07-04 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
    ]
