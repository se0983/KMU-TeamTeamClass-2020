# Generated by Django 3.0.7 on 2020-06-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trash_api', '0004_gps'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lastcheck',
            field=models.IntegerField(null=True),
        ),
    ]
