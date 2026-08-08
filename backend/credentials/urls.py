from django.urls import path

from .views import home, login_user,profile, questionsViews,update_about_me,profile_view,job,event,logout_user,generate_resume,update_profile_image,save_contact_details,quiz
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", login_user, name="login_user"),
    path("home/", home, name="home"),  # Updated path to match redirection
    path("profile/",profile,name="profile"),
    path("update_about_me/", update_about_me, name="update_about_me"),
    path("profile/", profile_view, name="profile"),
    path("job/", job, name="job"),
    path("event/", event, name="event"),
    path('logout/',logout_user, name='logout'),
    path('generate-resume/',generate_resume, name='generate_resume'),
    path('update-profile-image/', update_profile_image, name='update_profile_image'),
    path('save_contact_details/', save_contact_details, name='save_contact_details'),
   path("test/", quiz, name="test"),
   path("question_set/<str:username>/<str:quiz_type>/", questionsViews, name="question_set"),
   # path('resume/', generate_resume, name='generate_resume'),


]   

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)