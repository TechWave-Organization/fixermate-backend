# Generated by Django 4.2.1 on 2023-07-02 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.IntegerField(),
        ),
    ]
