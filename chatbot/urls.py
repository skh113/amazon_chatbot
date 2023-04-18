from rest_framework import routers
from django.views.generic import TemplateView
from django.urls import path

from .views import AnswerViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register("answers", viewset=AnswerViewSet, basename="answers")
router.register("questions", viewset=QuestionViewSet, basename="questions")

urlpatterns = router.urls
