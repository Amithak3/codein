from django.db import models
from django.contrib.auth.models import User


# Define the Problem model
class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    

    def __str__(self):
        return self.title

# Define the Solution model
class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Solution to {self.problem.title}"

# Define the TestCase model
class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.TextField()
    expected_output = models.TextField()

    def __str__(self):
        return f"Test Case for {self.problem.title}"

# Define the Submission model
class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.user.username} for {self.problem.title}"

# Define the CodeSubmission model
class CodeSubmission(models.Model):
    Language = models.CharField(max_length=10)
    input_data = models.TextField(null=True, blank=True)
    output_data = models.TextField(null=True, blank=True)
    code = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    verdict = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"CodeSubmission in {self.language} at {self.timestamp}"
