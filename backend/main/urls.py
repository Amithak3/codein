from django.urls import path, include
from main.views import question, question_detail

urlpatterns = [
    path('question/', question, name='question'),
    path('question/<int:question_id>/', question_detail, name='question_detail'),
    path('auth/', include('accounts.urls')),  # This line includes the auth URLs
    

]