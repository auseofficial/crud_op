# Generated by Django 5.1 on 2024-08-17 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0005_remove_student_number_student_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone_number',
        ),
    ]
