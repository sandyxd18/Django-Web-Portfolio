# Generated by Django 3.1.14 on 2024-05-04 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandy', '0002_auto_20240504_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='home',
            name='heading',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='home',
            name='name_1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='home',
            name='name_2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='project',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='vendor',
            field=models.CharField(default='', max_length=20),
        ),
    ]