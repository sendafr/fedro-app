from django.shortcuts import render, redirect
from.models import QuestionAnswer
from .forms import CreateQuestionAnswerForm, QuestionAnswerForm
from django.http import JsonResponse, HttpResponse
# Create your views here.

def my_pasio(request):
    questions = QuestionAnswer.objects.all()
    context={'questions':questions}
    return render(request, 'personal/my_pasio.html', context)

def fedo(request):
    return render(request, 'fedo.html')

"""def question_answer(request):
    if request.method == "POST":
        form = QuestionAnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("authy:question_answer_list")
    else:
        form = QuestionAnswerForm()
        return render(request, "question_answer.html", {"form": form})"""
    

  
def create_question_answer(request):
    form = CreateQuestionAnswerForm()

    if request.method == "POST":
        form = CreateQuestionAnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<em>New Question was created succesfully<em>")
        
    return render(request, "personal/create_question_answer.html", {"form": form})
  

def get_question_answer(request):
    questions = QuestionAnswer.objects.all()
    return JsonResponse({"questions": list(questions.values())})
