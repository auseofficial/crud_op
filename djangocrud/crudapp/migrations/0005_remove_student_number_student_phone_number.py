# Generated by Django 5.1 on 2024-08-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0004_alter_student_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='number',
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default=1, max_length=15, verbose_name='Student Phone Number'),
            preserve_default=False,
        ),
    ]
