# Generated by Django 4.1.4 on 2023-02-04 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enter_leave',
            name='enter',
            field=models.CharField(max_length=100, verbose_name='Enter-Time'),
        ),
        migrations.AlterField(
            model_name='enter_leave',
            name='leave',
            field=models.CharField(max_length=100, verbose_name='Leave-Time'),
        ),
    ]
