from django.contrib import admin

# Register your models here.
from credentials.models import Login, Question, Quiz, UserSubmission
from credentials.models import Profile, Contact, Experience, Job,Event

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'category')
    list_filter = ('category',)
    search_fields = ('question_text', 'category')

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration_in_minutes')
    search_fields = ('title',)
    filter_horizontal = ('questions',)

class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ('username', 'score', 'submitted_at' , 'category') 
    list_filter = ('category',)
    

admin.site.register(Login)
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Experience)
admin.site.register(Event)
admin.site.register(Job)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(UserSubmission, UserSubmissionAdmin)




