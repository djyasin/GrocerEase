# Generated by Django 4.0.1 on 2022-01-22 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_list_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='users',
            new_name='user',
        ),
    ]
