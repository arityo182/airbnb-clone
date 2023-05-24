# Generated by Django 4.1.7 on 2023-05-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_avatar_user_bio_user_gender"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="birthdate",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="currency",
            field=models.CharField(
                blank=True,
                choices=[("usd", "USD"), ("krw", "KRW")],
                default="usd",
                max_length=3,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="language",
            field=models.CharField(
                blank=True,
                choices=[("en", "English"), ("kr", "Korean")],
                max_length=2,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="superhost",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
                max_length=10,
                null=True,
            ),
        ),
    ]