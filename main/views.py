from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import Bug
from .forms import login_form, bug_creation_form, register_form

# Create your views here.

def home_page(request):
    recent_bug_reports = Bug.objects.order_by('-date_reported')[:20]
    context = {
        'recent_bug_reports': recent_bug_reports,
    }
    return render(request, 'main/home_page.html', context)

# def sort_by_id(request):
#     recent_bug_reports = Bug.objects.order_by('-id')[:20]
#     context = {
#         'recent_bug_reports': recent_bug_reports,
#     }
#     return render(request, 'main/home_page_by_id.html', context)

def detail(request, bug_id):
    bug=get_object_or_404(Bug, pk=bug_id)
    return render(request, 'main/detail.html', {'bug':bug})

def login_view(request):
    return render(request, 'main/login.html', {'form':login_form})

# def register_view(request):
#     print(request.POST)
#     if(request.password==request.confirm_Password):
#         return render(request, 'main/register.html', {'form':register_form})           # work with this later
#     else:
#         return render(request, 'main/pass_no_match.html')

def register_view(request):
    return render(request, 'main/register.html', {'form':register_form})


def new_bug(request):
    form = bug_creation_form(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'main/user_bug_creation.html', {'form':form})

# def new_bug(request):
#     return render(request, 'main/user_bug_creation.html')

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