from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from board.models import Attendance, Question


class AttendanceListView(TemplateView):
    template_name = "attendance/list.html"

    def get_context_data(self, **kwargs):

        context = {}

        attendances = Attendance.objects.all().order_by('-created_at')
        context['attendances'] = attendances

        return context
    

class AttendanceCreateView(TemplateView):
    template_name = "attendance/create.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        
        return context
    
    def post(self, request):
        name = request.POST.get('name')
        date = request.POST.get('date')
        status = request.POST.get('status')
        reason = request.POST.get('reason')

        Attendance.objects.create(
            name=name,
            date=date,
            status=status,
            reason=reason
        )
        
        # 메시지 설정
        messages.success(request, "성공했습니다.")
        messages.info(request, "추가 메시지")

        return redirect('attendance_list')


class QuestionListView(TemplateView):
    template_name = "question/list.html"

    def get_context_data(self, **kwargs):

        context = {}

        questions = Question.objects.all().order_by("-created_at")
        context['questions'] = questions

        return context
    

class QuestionDetailView(TemplateView):
    template_name = "question/create.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        question_id = kwargs['id']
        question = get_object_or_404(Question, id=question_id)
        context['question'] = question

        return context
    

class QuestionCreateView(TemplateView):
    template_name = "question/list.html"

    def get_context_data(self, **kwargs):

        context = {}

        return context

        
    
    def post(self, request):
        return redirect('question_list')
    

def index(request):
    return redirect("attendance_list")