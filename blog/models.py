from django.db import models
from mdeditor.fields import MDTextField


class Post(models.Model):
    title = models.CharField(
        "タイトル", max_length=50,
    )
    body = MDTextField("本文")
    created_at = models.DateTimeField(
        "作成日時", auto_now_add=True,
    )
