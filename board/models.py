from typing import Iterable, Optional
from django.db import models
from enum import Enum



class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="생성일", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="갱신일", auto_now=True)

    class Meta:
        abstract = True


class Profile(BaseModel):
    name = models.CharField(verbose_name="이름", max_length=10)
    age = models.PositiveSmallIntegerField(verbose_name="나이")
    email = models.EmailField(verbose_name="이메일", blank=True)
    description = models.TextField(verbose_name="소개", blank=True)

    def __str__(self):
        return f"{self.name}의 프로필"
    
    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        # 저장 될 때마다 수행되는 로직
        # 결제에서 order_code -> 결제 주문서가 생성될 때 난수 값으로 만듦
        return super().save(force_insert, force_update, using, update_fields)
    
    def get_name(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "프로필"
        verbose_name_plural = "프로필 목록"


class Attendance(BaseModel):
    ATTENDANCE = 1
    ABSENT = 2
    PARTIAL = 3
    ATTENDANCE_TYPE = [
        (ATTENDANCE, "출석"),
        (ABSENT, "결석 (사유 필히 작성)"),
        (PARTIAL, "일부 일정 불참 (사유 필히 작성)"),
    ]
    name = models.CharField(verbose_name="이름", max_length=10)
    date = models.DateField(verbose_name="날짜")
    status = models.PositiveSmallIntegerField(verbose_name="출석여부", choices=ATTENDANCE_TYPE, unique=True)
    reason = models.TextField(verbose_name="사유", null=True, blank=True)

    def __str__(self):
        return self.get_attendance_type_display()

    class Meta:
        verbose_name = "카테고리"
        verbose_name_plural = "카테고리 목록"


class Question(BaseModel):
    title = models.CharField(verbose_name="제목", max_length=30)
    content = models.TextField(verbose_name="내용")
    screenshot = models.ImageField(verbose_name="스크린샷", default="/static/img/명탐정피카20.gif")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "질문"
        verbose_name_plural = "질문 목록"
