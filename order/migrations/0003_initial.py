# Generated by Django 4.0.4 on 2022-05-25 01:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("transaction", "0001_initial"),
        ("order", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="transaction",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="transaction.transaction",
            ),
        ),
    ]
