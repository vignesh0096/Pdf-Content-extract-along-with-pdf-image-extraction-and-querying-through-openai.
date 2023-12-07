# Generated by Django 4.2.7 on 2023-12-04 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_extract_app', '0002_alter_pdfs_id_alter_pdfs_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfs',
            name='pdf1',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='pdfs',
            name='pdf2',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='pdfs',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]