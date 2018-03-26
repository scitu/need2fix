# Generated by Django 2.0.3 on 2018-03-26 08:30

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
                ('building', models.CharField(max_length=32)),
                ('floor', models.CharField(max_length=32)),
                ('room', models.CharField(blank=True, max_length=32, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('done_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'รับเรื่อง'), ('2', 'ดำเนินการ'), ('3', 'เสร็จสิ้น')], max_length=1)),
                ('division', models.CharField(blank=True, choices=[('1', 'ฝ่ายเทคโนโลยีสารสนเทศ'), ('2', 'ฝ่ายอาคารและสถานที่')], max_length=2, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=app.models.get_upload_path)),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_set', to=settings.AUTH_USER_MODEL)),
                ('requester', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='request_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
