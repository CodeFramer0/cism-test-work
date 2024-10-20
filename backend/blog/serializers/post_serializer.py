from rest_framework import serializers

from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "likes_count",
        ]

    def validate_title(self, value):
        """Валидация названия"""
        if not value:
            raise serializers.ValidationError("Название поста не может быть пустым.")
        return value

    def validate_content(self, value):
        "Валидация содержания"
        if len(value) < 10:
            raise serializers.ValidationError(
                "Содержание статьи не может быть меньше 10 символов."
            )
        return value
