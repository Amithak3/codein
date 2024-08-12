from django.urls import path, include
from django.contrib import admin
from . import views
from main.views import question, question_detail

urlpatterns = [
    path('question/', question, name='question'),
    path('question/<int:question_id>/', question_detail, name='question_detail'),
    path('auth/', include('accounts.urls')),  # This line includes the auth URLs
    path('admin/', admin.site.urls),
    

]