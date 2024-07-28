from django.urls import path
from main.views import question, question_detail

urlpatterns = [
    path('all/', question, name='question'),
    path('all/<int:question_id>/', question_detail, name='question_details'),

    
]