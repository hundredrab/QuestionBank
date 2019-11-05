from rest_framework import serializers

from .models import QuestionPaper, Question, Tag, QuestionSet

class QuestionSerializer(serializers.ModelSerializer):
    """Serializer for Question model."""
    class Meta:
        model = Question
        fields = '__all__'


class QuestionPaperSerializer(serializers.ModelSerializer):
    """Serializer for Question Paper model."""
    questions = QuestionSerializer(many=True)

    class Meta:
        model = QuestionPaper
        fields = '__all__'


class QuestionSetSerializer(serializers.ModelSerializer):
    """Serializer for Question Paper model."""
    questions = QuestionSerializer(many=True)

    class Meta:
        model = QuestionSet
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag model."""
    class Meta:
        model = Tag
        fields = '__all__'

class TagTree(serializers.ModelSerializer):
    """Serializer for a nested Tag tree."""

    subcategories = serializers.SerializerMethodField(
        read_only=True, method_name="get_child_categories")
    class Meta:
        model = Tag
        fields = '__all__'

    def get_child_categories(self, obj):
        print(obj.children.all())
        serializer = TagTree(
            instance=obj.children.all(),
            many=True
        )
        return serializer.data
