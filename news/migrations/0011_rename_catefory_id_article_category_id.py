# Generated by Django 3.2.9 on 2021-11-13 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20211113_0748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='catefory_id',
            new_name='category_id',
        ),
    ]