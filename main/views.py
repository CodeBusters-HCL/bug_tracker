from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import Bug

# Create your views here.

def home_page(request):
    recent_bug_reports = Bug.objects.order_by('-date_reported')[:20]
    context = {
        'recent_bug_reports': recent_bug_reports,
    }
    return render(request, 'main/home_page.html', context)

def detail(request, bug_id):
    bug=get_object_or_404(Bug, pk=bug_id)
    return render(request, 'main/detail.html', {'bug':bug})

def login_view(request):
    return render(request, 'main/login.html')

def register_view(request):
    return render(request, 'main/register.html')

def new_bug(request):
    return render(request, 'main/user_bug_creation.html')

# def welcome_view(request,username):
#     username=request.GET(username)
#     return render(request, 'main/welcome.html', {'user':username})


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     #output = ', '.join([q.question_text for q in latest_question_list])
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)