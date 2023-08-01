from django.db import models
from django.contrib.auth import get_user_model
from gpt.models import QnA

User = get_user_model()

# Create your models here.

# class Post(models.Model):
#     gpt = models.ForeignKey(QnA, on_delete=models.CASCADE)
#     # 보낸 질문의 일부를 제목으로
#     # title = models.CharField()
#     # 보낸 질문
#     question = models.
#     # 받은 대답
#     # answer = models.ForeignKey(gpt_a, on_delete=models.DO_NOTHING)
#     # 질문을 보낸 사람
#     writer = models.ForeignKey(User, on_delete=models.CASCADE)
#     # 질문을 보낸 시간
#     create_at = models.DateTimeField(auto_now_add=True)
#     # 가용여부(List로 출력되거나 검색이 가능한지)
#     visible = models.BooleanField(default=True)
    
#     def __str__(self):
#         return self