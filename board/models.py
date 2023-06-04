from enum import Enum
from datetime import datetime, date
from django.db import models
from django.core.exceptions import ValidationError


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="생성일", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="갱신일", auto_now=True)

    class Meta:
        abstract = True


class Attendance(BaseModel):
    ATTENDANCE = 1
    ABSENT = 2
    PARTIAL = 3
    ATTENDANCE_TYPE = [
        (ATTENDANCE, "출석"),
        (ABSENT, "결석"), # 사유 필히 작성
        (PARTIAL, "일부 일정 불참"), # 사유 필히 작성
    ]
    name = models.CharField(verbose_name="이름", max_length=5)
    date = models.DateField(verbose_name="날짜")
    status = models.PositiveSmallIntegerField(verbose_name="출석여부", choices=ATTENDANCE_TYPE)
    reason = models.TextField(verbose_name="사유", null=True, blank=True)

    def __str__(self):
        return self.get_status_display()
    
    def clean_reason(self):
        if self.status != 1 and not self.reason:
            raise ValidationError("결석 및 일부 불참의 경우, 사유를 반드시 작성해야 합니다.")
    
    def clean_date(self):
        if self.date > datetime.today().date():
            raise ValidationError("오늘 이후의 출결을 미리 등록할 수 없습니다. ")


    class Meta:
        verbose_name = "출결"
        verbose_name_plural = "출결 목록"


class Question(BaseModel):
    title = models.CharField(verbose_name="제목", max_length=30)
    content = models.TextField(verbose_name="내용")
    screenshot = models.ImageField(verbose_name="스크린샷", default='default_img/명탐정피카20.gif')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "질문"
        verbose_name_plural = "질문 목록"
