# Generated by Django 3.0.3 on 2020-05-07 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0006_auto_20200508_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
