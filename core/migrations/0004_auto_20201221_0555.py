# Generated by Django 3.1.4 on 2020-12-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201221_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Year',
            field=models.IntegerField(max_length=7),
        ),
    ]
