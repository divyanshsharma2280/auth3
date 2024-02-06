# Generated by Django 5.0 on 2024-01-10 20:20

import ckeditor_uploader.fields
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadCast_Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name': 'BroadCast Email to all Member',
                'verbose_name_plural': 'BroadCast Email',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='password_confirmation',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]