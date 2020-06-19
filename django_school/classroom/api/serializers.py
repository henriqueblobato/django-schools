from rest_framework.serializers import ModelSerializer
from classroom.models import Quiz

class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('owner','name','subject',)