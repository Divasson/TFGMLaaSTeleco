# Generated by Django 4.1.7 on 2023-03-28 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crearModelos", "0005_modelosmachinelearning_ensemble_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelosmachinelearning",
            name="ensemble_model",
            field=models.BooleanField(default=False),
        ),
    ]