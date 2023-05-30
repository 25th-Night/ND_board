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
        query_string = request.GET.get('qs')
        context = {
            "method": request.method,
            "user": request.user,
            "greeting": "안녕하세요",
            # "code": code,
            # "name": name,
            "query_string" : query_string
        }
        return render(request, "index.html", context)
    if request.method == 'POST':
        return HttpResponse("index by POST FBV function called")
    
def index_function2(request):
    if request.method == 'GET':
        query_string = request.GET.get('qs')
        context = {
            "method": request.method,
            "user": request.user,
            "greeting": "안녕하세요",
            "query_string" : query_string
        }
        return render(request, "index.html", context)
    if request.method == 'POST':
        return HttpResponse("index by POST FBV function2 called")
    

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