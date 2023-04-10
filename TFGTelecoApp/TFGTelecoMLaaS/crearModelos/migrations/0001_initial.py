# Generated by Django 4.1.7 on 2023-04-10 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("createOpenProject", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ModelosMachineLearning",
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
                ("modelo", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=200)),
                ("optuna", models.BooleanField(default=False)),
                ("supports_y_ohe", models.BooleanField(default=False)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                ("metrica_valorar", models.FloatField(blank=True, null=True)),
                ("ensemble_model", models.BooleanField(default=False)),
                (
                    "ensemble_models_made",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "proyecto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Proyecto",
                        to="createOpenProject.project",
                    ),
                ),
            ],
            options={
                "unique_together": {("proyecto", "name")},
            },
        ),
    ]
