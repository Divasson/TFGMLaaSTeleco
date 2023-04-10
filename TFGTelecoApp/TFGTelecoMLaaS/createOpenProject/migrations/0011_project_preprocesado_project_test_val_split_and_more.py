# Generated by Django 4.1.7 on 2023-02-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("createOpenProject", "0010_project_tipos_de_modelos"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="preprocesado",
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name="project",
            name="test_val_split",
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="train_test_split",
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
    ]