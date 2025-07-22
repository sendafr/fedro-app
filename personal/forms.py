from django.contrib.auth.forms import forms
from django.template.defaultfilters import title

from .models import QuestionAnswer


class QuestionAnswerForm(forms.Form):
    class Meta:
        model = QuestionAnswer
        fields = ["title", "question", "answer", "priority"]
        widgets = {title: forms.TextInput(attrs={"class": "form-control"})}

    def save(self):
        pass


class CreateQuestionAnswerForm(forms.ModelForm):
    class Meta:
        model = QuestionAnswer
        fields = ["title", "question", "answer", "priority"]
