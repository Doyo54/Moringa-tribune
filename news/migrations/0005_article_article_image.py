# Generated by Django 4.0.4 on 2022-05-25 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(null=True, upload_to='articles/'),
        ),
    ]