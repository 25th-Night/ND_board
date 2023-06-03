from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from board.models import Attendance, Question
from board.utils import Pagination


class AttendanceListView(TemplateView):
    template_name = "attendance/list.html"
    data_per_page = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

        attendances = Attendance.objects.all().order_by('-created_at')
        # Pagination
        page, page_obj, page_num_list, empty_row_count = Pagination(self.request, attendances, self.data_per_page).paginate

        context["page"] = page
        context["page_obj"] = page_obj
        context["page_num_list"] = page_num_list
        context['empty_row_count'] = empty_row_count

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
        messages.success(request, "등록에 성공했습니다.")

        return redirect('attendance_list')


class QuestionListView(TemplateView):
    template_name = "question/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

        questions = Question.objects.all().order_by("-created_at")
        context['questions'] = questions

        return context
    

class QuestionDetailView(TemplateView):
    template_name = "question/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        question_id = kwargs['id']
        question = get_object_or_404(Question, id=question_id)
        context['question'] = question

        return context
    

class QuestionCreateView(TemplateView):
    template_name = "question/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        screenshot = request.FILES.get('screenshot')

        if not screenshot:
            Question.objects.create(
                title=title,
                content=content,
            )
        else:
            Question.objects.create(
                title=title,
                content=content,
                screenshot=screenshot,
            )

        # 메시지 설정
        messages.success(request, "등록에 성공했습니다.")

        return redirect('question_list')
    

def index(request):
    return redirect("attendance_list")