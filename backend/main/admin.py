from django.contrib import admin
from main.models import Problem, Solution, TestCase, CodeSubmission

admin.site.register(Problem)
admin.site.register(CodeSubmission)
admin.site.register(TestCase)