# Generated by Django 4.1.7 on 2023-03-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("createOpenProject", "0012_alter_project_tipos_de_modelos"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="treat_na_dict",
            field=models.FileField(blank=True, upload_to="documents/treat_na/"),
        ),
    ]