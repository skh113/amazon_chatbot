from json import JSONDecodeError

from openai import api_key, Model, Completion
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, views, status
from django.conf import settings

from .models import Answer, Question
from .serializers import AnswerSerializer, QuestionSerializer, ApiTestSerializer


class AnswerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Answer.objects.all().order_by("id")
    serializer_class = AnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("id")
    serializer_class = QuestionSerializer


class OpenAIAPIView(APIView):
    def post(self, request):
        api_key = settings.OPENAI_API_KEY
        prompt = request.data.get('prompt', '')
        model_engine = request.data.get('model_engine', 'text-davinci-003')
        max_tokens = request.data.get('max_tokens', 1000)
        temperature = request.data.get('temperature', 0.5)
        n = request.data.get('n', 1)
        stop = request.data.get('stop', None)
        presence_penalty = request.data.get('presence_penalty', 0)
        frequency_penalty = request.data.get('frequency_penalty', 0)

        if not prompt:
            return Response({'error': 'Prompt is required'})

        try:
            model = Model(engine=model_engine, api_key=api_key)
            response = model.generate(
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                n=n,
                stop=stop,
                presence_penalty=presence_penalty,
                frequency_penalty=frequency_penalty
            )
        except Exception as e:
            return Response({'error': str(e)})

        print(Response({'response': response.choices[0].text}))
        return Response({'response': response.choices[0].text})
