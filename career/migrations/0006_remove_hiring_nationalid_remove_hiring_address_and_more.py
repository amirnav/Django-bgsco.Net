# Generated by Django 5.0.3 on 2024-03-13 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0005_remove_hiring_fileupload_alter_hiring_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hiring',
            name='NationalId',
        ),
        migrations.RemoveField(
            model_name='hiring',
            name='address',
        ),
        migrations.RemoveField(
            model_name='hiring',
            name='birthdayDate',
        ),
        migrations.RemoveField(
            model_name='hiring',
            name='country',
        ),
        migrations.RemoveField(
            model_name='hiring',
            name='email',
        ),
        migrations.RemoveField(
            model_name='hiring',
            name='fatherName',
        ),
        migrations.RemoveField(
            model_name='hiring',
            name='marriageSituate',
        ),
        migrations.RemoveField(
            model_name='hiring',
            name='phone',
        ),
    ]
