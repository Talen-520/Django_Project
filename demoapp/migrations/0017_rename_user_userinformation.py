# Generated by Django 4.2.4 on 2023-09-02 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0016_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='userinformation',
        ),
    ]
