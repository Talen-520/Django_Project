# Generated by Django 4.2.4 on 2023-08-28 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0009_alter_new_menu_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_menu',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='demoapp.new_menucategory'),
        ),
    ]
