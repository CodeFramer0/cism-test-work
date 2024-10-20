from django.db import models

from .post import Post


class Like(models.Model):
    """Лайк поста"""

    post = models.ForeignKey(
        Post, verbose_name="Пост", related_name="likes", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"

    def __str__(self):
        return f"Лайк поста {self.post.title}"
