from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
# from django.template import loader
from django.http import Http404

from .models import Question, Choice
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question Does not Exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    response = "you are looking at the results of the question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you are voting for the question %s" % question_id)

def login(request):
    return render(request, 'polls/login.html')

def register(request):
    return render(request, 'polls/registration.html')