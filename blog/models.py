from django.db import models
from mdeditor.fields import MDTextField
import uuid


class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    # postgres対応
    temp_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(
        "タイトル", max_length=50,
    )
    category = models.ForeignKey(
        Category, verbose_name='カテゴリー',
        on_delete=models.PROTECT
    )
    body = MDTextField("本文")
    created_at = models.DateTimeField(
        "作成日時", auto_now_add=True,
    )
