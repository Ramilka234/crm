# Generated by Django 4.2.6 on 2023-10-25 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmbackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='min_prepayment',
            field=models.FloatField(default=0),
        ),
    ]
