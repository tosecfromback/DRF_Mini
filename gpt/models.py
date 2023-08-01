from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class QnA(models.Model):
    question = models.TextField()
    qeustion_time = models.DateTimeField(auto_now_add=True)
    answer = models.TextField()
    answer_time = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self