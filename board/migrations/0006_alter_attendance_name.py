# Generated by Django 4.2.1 on 2023-06-03 10:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0005_alter_attendance_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="name",
            field=models.CharField(max_length=5, verbose_name="이름"),
        ),
    ]
