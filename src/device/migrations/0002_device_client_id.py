# Generated by Django 3.2.19 on 2023-07-16 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='client_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
    ]