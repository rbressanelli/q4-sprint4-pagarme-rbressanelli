# Generated by Django 4.0.4 on 2022-05-25 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="is_Active",
        ),
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
