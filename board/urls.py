from django.urls import path
from board.views import *

urlpatterns = [
    path('attendance/', AttendanceListView.as_view(), name="attendance_list"),
    path('attendance/create/', AttendanceCreateView.as_view(), name="attendance_create"),
    path('question/', QuestionListView.as_view(), name="question_list"),
    path('question/<int:id>/', QuestionDetailView.as_view(), name="question_detail"),
    path('question/create/', QuestionCreateView.as_view(), name="question_create"),


]