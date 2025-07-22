from django.urls import path
from personal.views import(
     my_pasio,
     create_question_answer,
     get_question_answer,
     fedo,
     )


urlpatterns =[
    path("", my_pasio, name="my_pasio"),
    path("create_question_answer", create_question_answer, name="create_question_answer"),
    path("get_question_answer", get_question_answer, name="get_question_answer"),
    path("fedo", fedo, name="fedo")
]
