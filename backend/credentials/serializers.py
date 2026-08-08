from rest_framework import serializers
from .models import Question, Quiz, UserSubmission

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)  # Nested questions

    class Meta:
        model = Quiz
        fields = '__all__'

class UserSubmissionSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField()  # Shows actual username
    quiz = serializers.StringRelatedField()  # Shows quiz title instead of ID

    class Meta:
        model = UserSubmission
        fields = '__all__'

    def to_representation(self, instance):
        """Optimize DB queries using select_related."""
        instance = UserSubmission.objects.select_related('username', 'quiz').get(id=instance.id)
        return super().to_representation(instance)
