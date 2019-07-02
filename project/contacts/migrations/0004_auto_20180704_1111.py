# Generated by Django 2.0.6 on 2018-07-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_remove_document_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(default='documents/default.jpg', upload_to='documents/'),
        ),
    ]
