from rest_framework import serializers

from .models import QuestionPaper, Question

class QuestionPaperSerializer(serializers.ModelSerializer):
    """Serializer for Question Paper model."""
    class Meta:
        model = QuestionPaper
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer for Question model."""
    class Meta:
        model = Question
        fields = '__all__'
