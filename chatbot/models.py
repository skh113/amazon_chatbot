from django.db import models


class Question(models.Model):
    question = models.TextField(null=False, blank=False, default="")
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Question was: {self.question}"


class Answer(models.Model):
    answer = models.TextField(default="")
    question_number = models.OneToOneField(Question, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Answer was: {self.answer}"
