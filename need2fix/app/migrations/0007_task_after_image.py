# Generated by Django 2.0.6 on 2018-10-02 09:22

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180925_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='after_image',
            field=models.ImageField(blank=True, null=True, upload_to=app.models.get_upload_path),
        ),
    ]