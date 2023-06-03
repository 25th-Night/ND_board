
from datetime import datetime, date, timedelta

from django.test import TestCase, Client
from django.urls import reverse
from django.core.exceptions import ValidationError
from board.models import Attendance
from board.views import AttendanceListView
from board.utils import Pagination


class AttendanceModelTest(TestCase):
    def setUp(self):
        today = datetime.today().date()
        self.yesterday = today - timedelta(days=1)
        self.tomorrow = today + timedelta(days=1)

    def test_clean_method(self):
        attendance = Attendance(name="ABC", date=self.yesterday, status=Attendance.ATTENDANCE)
        attendance.clean_reason()

        attendance = Attendance(name="DEF", date=self.yesterday, status=Attendance.ABSENT, reason="개인 사정")
        attendance.clean_reason()

        attendance = Attendance(name="GHI", date=self.yesterday, status=Attendance.PARTIAL, reason="직장 일정")
        attendance.clean_reason()

        attendance = Attendance(name="JKL", date=self.yesterday, status=Attendance.ABSENT)
        with self.assertRaises(ValidationError):
            attendance.clean_reason()

        attendance = Attendance(name="MNO", date=self.yesterday, status=Attendance.PARTIAL)
        with self.assertRaises(ValidationError):
            attendance.clean_reason()

        attendance = Attendance(name="ABC", date=self.tomorrow, status=Attendance.ATTENDANCE)
        with self.assertRaises(ValidationError):
            attendance.clean_date()


class AttendanceListViewTest(TestCase):
    def setUp(self):
        data_num = 17
        for i in range(data_num):
            Attendance.objects.create(
                name=f"Name {i}",
                date=date(2023, 1, 1),
                status= i%3 + 1,
                reason="Reason"
            )
        
        self.attendances = Attendance.objects.all()

    def test_pagination(self):
        response = self.client.get("/attendance/")
        page_nums = response.context['page_num_list']
        for page_num in page_nums:
            each_response = self.client.get("/attendance/?page=" + str(page_num))
            if page_num == page_nums[-1]:
                self.assertEqual(self.attendances.count() % AttendanceListView.data_per_page, len(each_response.context['page_obj']))
                break
            self.assertEqual(AttendanceListView.data_per_page, len(each_response.context['page_obj']))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'attendance/list.html')
        self.assertContains(response, '출석')
        self.assertContains(response, '결석')
        self.assertContains(response, '일부 일정 불참')
        self.assertNotContains(response, '지각')


class AttendanceCreateViewTest(TestCase):
    def setUp(self):
        data = None

    def test_post(self):
        form_data = dict(
                        name= "테스터",
                        date = "2023-01-01",
                        status = "1",
                        reason = "없습니다."
                        )
        response = self.client.post("/attendance/create/", form_data)

        attendance = Attendance.objects.first()

        self.assertEqual(attendance.name, '테스터')
        self.assertEqual(attendance.date, date(2023, 1, 1))
        self.assertEqual(attendance.status, 1)
        self.assertEqual(attendance.reason, '없습니다.')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('attendance_list'), status_code=302, target_status_code=200)