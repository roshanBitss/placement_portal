# Create your views here.
from django.shortcuts import render

from credentials.models import Question
from credentials.serializers import QuestionSerializer
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse


def questionsView(request):
    quiz_type = request.session.get('quiz_type')

    if not quiz_type:
        return JsonResponse({"status": "error", "error": "Invalid data"}, status=400)
    
    # Fetch the user's profile using `username` instead of `user`
    try:
        question_obj = Question.objects.filter(category=quiz_type)
        serializers = QuestionSerializer(question_obj, many=True)
        print(serializers.data)
    except Exception as e:
        profile = None  # Set to None if no profile exists

    return render(request, 'myapp/questions.html', {'profile': profile})
    
    
    