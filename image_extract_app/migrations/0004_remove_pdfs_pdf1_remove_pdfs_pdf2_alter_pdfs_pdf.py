# Generated by Django 4.2.7 on 2023-12-05 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_extract_app', '0003_pdfs_pdf1_pdfs_pdf2_alter_pdfs_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdfs',
            name='pdf1',
        ),
        migrations.RemoveField(
            model_name='pdfs',
            name='pdf2',
        ),
        migrations.AlterField(
            model_name='pdfs',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
