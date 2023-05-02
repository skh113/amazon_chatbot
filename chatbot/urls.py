from rest_framework import routers
from django.views.generic import TemplateView
from django.urls import path, include

from .views import AnswerViewSet, QuestionViewSet, OpenAIAPIView

router = routers.DefaultRouter()
router.register("answers", viewset=AnswerViewSet, basename="answers")
router.register("questions", viewset=QuestionViewSet, basename="questions")

urlpatterns = [
    path("", include(router.urls)),
    path("api/", OpenAIAPIView.as_view(), name="api"),
]
