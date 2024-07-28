from django import forms 
from main.models import CodeSubmission

LANGUAGE_CHOICES = {
    ("py", "Python"),
    ("c", "C"),
    ("cpp", "C++")
}

class CodeSubmissionForm(forms.ModelForm):
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)

    class Meta:
        model = CodeSubmission
        fields = ["Language", "code", "input_data"]