# Generated by Django 4.2.4 on 2023-08-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0011_alter_new_menu_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('time_log', models.TimeField(help_text='enter exact time ')),
            ],
        ),
    ]
