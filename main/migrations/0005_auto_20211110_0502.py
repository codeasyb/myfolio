# Generated by Django 3.2.9 on 2021-11-10 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211110_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='about',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='main',
            name='facebook',
            field=models.CharField(default=' ', max_length=120),
        ),
        migrations.AlterField(
            model_name='main',
            name='links',
            field=models.CharField(default=' ', max_length=160),
        ),
        migrations.AlterField(
            model_name='main',
            name='telephone',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='main',
            name='twitter',
            field=models.CharField(default=' ', max_length=120),
        ),
        migrations.AlterField(
            model_name='main',
            name='youtube',
            field=models.CharField(default=' ', max_length=120),
        ),
    ]
