# Generated by Django 4.2.9 on 2024-02-17 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_menu_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='name_item',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='name',
            new_name='name_menu',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
    ]