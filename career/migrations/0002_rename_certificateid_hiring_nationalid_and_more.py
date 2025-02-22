# Generated by Django 5.0.3 on 2024-03-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hiring',
            old_name='certificateId',
            new_name='NationalId',
        ),
        migrations.AddField(
            model_name='hiring',
            name='fileUpload',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='hiring',
            name='country',
            field=models.CharField(blank=True, choices=[('SN', 'Single'), ('MR', 'Married')], max_length=50, null=True, verbose_name='Country'),
        ),
    ]
