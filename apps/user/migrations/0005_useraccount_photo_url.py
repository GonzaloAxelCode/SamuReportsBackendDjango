# Generated by Django 3.2.16 on 2023-07-10 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20230709_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='photo_url',
            field=models.CharField(default='https://res.cloudinary.com/ddksrkond/image/upload/v1688411778/default_dfvymc.webp', max_length=255),
        ),
    ]