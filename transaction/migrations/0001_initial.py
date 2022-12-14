# Generated by Django 4.0.4 on 2022-05-25 01:04

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("paymentinfo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("amount", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "payment_info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="paymentinfo.paymentinfo",
                    ),
                ),
            ],
        ),
    ]
