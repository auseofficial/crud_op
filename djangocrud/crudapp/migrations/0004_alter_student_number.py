# Generated by Django 5.1 on 2024-08-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_alter_student_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='number',
            field=models.BigIntegerField(max_length=15, verbose_name='Student Number'),
        ),
    ]
