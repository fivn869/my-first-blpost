# Generated by Django 3.0.7 on 2020-06-23 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('blog', models.TextField(max_length=258)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('us', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meeesage_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
