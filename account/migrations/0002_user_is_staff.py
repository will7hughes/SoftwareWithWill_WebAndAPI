# Generated by Django 2.2.16 on 2020-09-25 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='staff'),
        ),
    ]
