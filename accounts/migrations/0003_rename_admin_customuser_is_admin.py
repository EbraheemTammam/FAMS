# Generated by Django 4.2 on 2023-04-18 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='admin',
            new_name='is_admin',
        ),
    ]
