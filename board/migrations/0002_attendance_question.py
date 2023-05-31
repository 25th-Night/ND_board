# Generated by Django 4.2.1 on 2023-05-31 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
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
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성일"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="갱신일")),
                ("name", models.CharField(max_length=10, verbose_name="이름")),
                ("date", models.DateField(verbose_name="날짜")),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "출석"),
                            (2, "결석 (사유 필히 작성)"),
                            (3, "일부 일정 불참 (사유 필히 작성)"),
                        ],
                        unique=True,
                        verbose_name="출석여부",
                    ),
                ),
                ("reason", models.TextField(blank=True, null=True, verbose_name="사유")),
            ],
            options={
                "verbose_name": "카테고리",
                "verbose_name_plural": "카테고리 목록",
            },
        ),
        migrations.CreateModel(
            name="Question",
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
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성일"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="갱신일")),
                ("title", models.CharField(max_length=30, verbose_name="제목")),
                ("content", models.TextField(verbose_name="내용")),
                (
                    "screenshot",
                    models.ImageField(
                        default="/static/img/명탐정피카20.gif",
                        upload_to="",
                        verbose_name="스크린샷",
                    ),
                ),
            ],
            options={
                "verbose_name": "질문",
                "verbose_name_plural": "질문 목록",
            },
        ),
    ]