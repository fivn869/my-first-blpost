# Generated by Django 3.0.7 on 2020-07-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_poost'),
    ]

    operations = [
        migrations.AddField(
            model_name='poost',
            name='click_times',
            field=models.IntegerField(default=0),
        ),
    ]
