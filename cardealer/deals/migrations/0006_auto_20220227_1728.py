# Generated by Django 3.2.8 on 2022-02-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0005_auto_20220227_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='id',
        ),
        migrations.AddField(
            model_name='cars',
            name='cars_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
