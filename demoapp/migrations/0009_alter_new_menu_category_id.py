# Generated by Django 4.2.4 on 2023-08-28 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0008_menu_new_menucategory_new_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_menu',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='demoapp.new_menucategory'),
        ),
    ]
