# Generated by Django 2.2.1 on 2019-07-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190715_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='comment',
            field=models.TextField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
