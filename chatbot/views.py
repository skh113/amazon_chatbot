from rest_framework import viewsets

from .models import Answer, Question
from .serializers import AnswerSerializer, QuestionSerializer


class AnswerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Answer.objects.all().order_by("id")
    serializer_class = AnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("id")
    serializer_class = QuestionSerializer
