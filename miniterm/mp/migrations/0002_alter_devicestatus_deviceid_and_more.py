# Generated by Django 5.1.1 on 2024-10-04 03:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="devicestatus",
            name="deviceID",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="devicestatus",
            name="status",
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name="facerecognitionlogs",
            name="recongnitionid",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="facerecognitionlogs",
            name="userid",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="mp.accesspeople"
            ),
        ),
    ]
