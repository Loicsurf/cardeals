# Generated by Django 3.2.8 on 2022-02-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0008_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='image',
            field=models.FileField(default=1, upload_to=''),
        ),
    ]