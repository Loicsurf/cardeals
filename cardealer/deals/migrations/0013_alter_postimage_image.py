# Generated by Django 3.2.8 on 2022-02-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0012_cars_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.FileField(default=None, upload_to='static/assets/images'),
        ),
    ]