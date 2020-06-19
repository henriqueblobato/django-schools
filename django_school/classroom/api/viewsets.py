from rest_framework import viewsets
from classroom.models import Quiz
from rest_framework.response import Response

from .serializers import QuizSerializer

class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    # def get_queryset(self):
    #     return Quiz.objects.all()
