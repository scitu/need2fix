# Generated by Django 2.0.6 on 2018-09-18 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180712_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='contact',
            field=models.EmailField(blank=True, max_length=32, null=True),
        ),
    ]
