from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Like, Post
from ..serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.prefetch_related("likes").all()
    serializer_class = PostSerializer

    @action(detail=True, methods=["post", "delete"])
    def like(self, request, pk=None):
        """
        Создание или удаление лайка.

        POST /posts/{id}/like - поставить лайк посту

        DELETE /posts/{id}/like - убрать лайк с поста
        """
        post = self.get_object()

        # Костыль в угоду компактности кода, мог сделать иначе.
        # Но ради 2 эндпоинтов не хотелось портить структуру проекта :(
        # Я думаю, что в реальном проекте юзал бы APIView.
        if request.method == "POST":
            Like.objects.create(post=post)
            return Response(
                PostSerializer(instance=post).data,
                status=status.HTTP_201_CREATED,
            )

        elif request.method == "DELETE":
            like = Like.objects.filter(post=post).first()
            if not like:
                return Response(
                    {"detail": "У поста отсутствуют лайки."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
