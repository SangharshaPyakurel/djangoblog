# Generated by Django 4.1.7 on 2023-09-11 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='context',
            new_name='content',
        ),
    ]