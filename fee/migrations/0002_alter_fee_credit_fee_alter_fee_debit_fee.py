# Generated by Django 4.0.4 on 2022-05-25 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='credit_fee',
            field=models.FloatField(default=0.05),
        ),
        migrations.AlterField(
            model_name='fee',
            name='debit_fee',
            field=models.FloatField(default=0.03),
        ),
    ]