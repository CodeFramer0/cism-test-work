from django.contrib import admin

from ..models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """
    Лайки
    """

    list_display = ("post", "post__created_at")
    list_filter = ("post__created_at",)
    search_fields = ("post__title",)
