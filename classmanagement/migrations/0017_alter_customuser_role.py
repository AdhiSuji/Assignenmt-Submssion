# Generated by Django 5.1.6 on 2025-03-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classmanagement', '0016_alter_customuser_managers_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('student', 'Student'), ('teacher', 'Teacher')], default='student', max_length=20),
        ),
    ]
