# Generated by Django 4.2.5 on 2023-09-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_alter_healthprofile_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="healthprofile",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_picture/"
            ),
        ),
    ]
