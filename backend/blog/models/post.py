from django.db import models


class Post(models.Model):
    """Пост"""

    title = models.CharField(verbose_name="Заголовок поста", max_length=255)
    content = models.TextField("Текст поста")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title
