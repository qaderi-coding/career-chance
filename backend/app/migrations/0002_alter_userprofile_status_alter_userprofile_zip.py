# Generated by Django 4.2.4 on 2023-08-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zip',
            field=models.IntegerField(blank=True),
        ),
    ]
