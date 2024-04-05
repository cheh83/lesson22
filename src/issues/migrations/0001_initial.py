# Generated by Django 4.2.11 on 2024-04-05 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Issue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("status", models.PositiveSmallIntegerField()),
                (
                    "junior",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="junior_issue",
                        to="user.user",
                    ),
                ),
                (
                    "senior",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="senior_issues",
                        to="user.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "issue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issue_massege",
                        to="issues.issue",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_massege",
                        to="user.user",
                    ),
                ),
            ],
        ),
    ]
