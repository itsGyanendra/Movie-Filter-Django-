# Generated by Django 3.1.4 on 2020-12-21 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201220_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Year',
            field=models.CharField(max_length=7),
        ),
    ]
