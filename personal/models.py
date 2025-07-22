from django.db import models

# Create your models here.
PRIORITY = [
    ("L", "low"),
    ("M", "medium"),
    ("H", "high"),
]


class QuestionAnswer(models.Model):
    title = models.CharField(max_length=60)
    question = models.TextField(max_length=400)
    answer = models.TextField(max_length=300)
    priority = models.CharField(max_length=1, choices=PRIORITY)

    class Meta:
        verbose_name = "The Question, The Answer"
        verbose_name_plural = "User Questions, User Answers"

    def __str__(self):
        return self.title
