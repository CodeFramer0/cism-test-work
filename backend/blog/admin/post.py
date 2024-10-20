from django.contrib import admin

from ..models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Посты
    """

    list_display = ("title", "created_at", "total_likes")
    search_fields = ("title", "content")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)

    def total_likes(self, obj):
        """Подсчет общего числа лайков для поста"""
        return obj.likes.count()

    total_likes.short_description = "Количество лайков"
