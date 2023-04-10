# Generated by Django 4.1.7 on 2023-03-07 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (
            "createOpenProject",
            "0011_project_preprocesado_project_test_val_split_and_more",
        ),
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
                ("name", models.CharField(max_length=50)),
                ("optuna", models.BooleanField(default=False)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                ("balanced_accuracy", models.FloatField(blank=True, null=True)),
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