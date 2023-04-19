from django.db import models


class Answer(models.Model):
    answer = models.TextField(default="")
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Answer was: {self.answer}"


class Question(models.Model):
    question = models.TextField(null=False, blank=False, default="")
    answer_number = models.OneToOneField(Answer, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Question was: {self.question}"
