# Generated by Django 2.0.6 on 2018-07-04 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0015_auto_20180704_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(default='documents/avatar.svg', upload_to='documents/'),
        ),
    ]
