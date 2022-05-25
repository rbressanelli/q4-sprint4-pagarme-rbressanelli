# Generated by Django 4.0.4 on 2022-05-25 01:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('credit_fee', models.IntegerField(default=0.05)),
                ('debit_fee', models.IntegerField(default=0.03)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
