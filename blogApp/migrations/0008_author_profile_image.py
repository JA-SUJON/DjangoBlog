# Generated by Django 3.0.3 on 2020-05-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0007_auto_20200508_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile_image',
            field=models.FileField(default='', upload_to=''),
        ),
    ]