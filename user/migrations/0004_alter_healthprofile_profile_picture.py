# Generated by Django 4.2.5 on 2023-09-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_healthprofile_calories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="healthprofile",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/health_profiles/"
            ),
        ),
    ]
