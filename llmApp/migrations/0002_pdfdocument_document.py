# Generated by Django 5.0.3 on 2024-03-10 13:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('llmApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfdocument',
            name='document',
            field=models.FileField(default=django.utils.timezone.now, upload_to='pdf_documents/'),
            preserve_default=False,
        ),
    ]