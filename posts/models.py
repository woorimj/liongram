from django.db import models
from django.contrib.auth import get_user_model ## 사용자모델을 장고로 부터 가져옴

User = get_user_model() ## 사용자모델을 생성함

# 1. 게시글
class Post(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)

# 2. 댓글
class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일')
    # 게시글과의 연결
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE)
    # 사용자와의 연결
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE)
