from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Function Based View
# FBV
def index_function(request, code, name):
    if request.method == 'GET':
        # return HttpResponse("index by GET FBV function called")
        context = {
            "method": request.method,
            "user": request.user,
            "greeting": "안녕하세요",
            "code": code,
            "name": name
        }
        return render(request, "index.html", context)
    if request.method == 'POST':
        return HttpResponse("index by POST FBV function called")
    

# Class Based View
# CBV
@method_decorator(csrf_exempt, name='dispatch')
class IndexClass(View):
    def get(self, request):
        return HttpResponse("index by GET CBV function called")
    
    def post(self, request):
        return HttpResponse("index by POST CBV function called")
    
class IndexClass2(TemplateView):
    template_name = "index.html"

    def get(self, request):
        response = super(IndexClass2, self).get(self, request)
        return response