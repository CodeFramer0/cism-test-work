from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Like, Post


class PostAPITests(APITestCase):
    def setUp(self):
        """
        Тестовые данные
        """
        self.valid_post_data = {
            "title": "Привет мир!",
            "content": "Lorem Ipsum - это текст, часто используемый в печати и вэб-дизайне.",
        }
        self.invalid_post_data = {"title": "...", "content": "..."}

        self.post = Post.objects.create(**self.valid_post_data)

    def test_create_post_valid(self):
        """
        Создание поста с валидными данными.
        """
        response = self.client.post("/api/posts/", self.valid_post_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_create_post_invalid(self):
        """
        Создание поста с невалидными данными.
        """
        response = self.client.post("/api/posts/", self.invalid_post_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Post.objects.count(), 1)

    def test_get_posts(self):
        """
        Получение списка всех постов.
        """
        response = self.client.get("/api/posts/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_post_detail(self):
        """
        Получение поста по ID.
        """
        response = self.client.get(f"/api/posts/{self.post.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.post.title)

    def test_update_post(self):
        """
        Обновление поста.
        """
        updated_data = {
            "title": "Обновленный пост",
            "content": "Содержимое обновленного поста.",
        }
        response = self.client.put(f"/api/posts/{self.post.id}/", updated_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.post.refresh_from_db()
        self.assertEqual(self.post.title, updated_data["title"])
        self.assertEqual(self.post.content, updated_data["content"])

    def test_delete_post(self):
        """
        Удаление поста.
        """
        response = self.client.delete(f"/api/posts/{self.post.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_like_post(self):
        """
        Добавление лайка.
        """
        response = self.client.post(f"/api/posts/{self.post.id}/like/")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 1)

    def test_unlike_post(self):
        """
        Удаление лайка.
        """
        self.client.post(f"/api/posts/{self.post.id}/like/")

        response = self.client.delete(f"/api/posts/{self.post.id}/like/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Like.objects.count(), 0)

    def test_unlike_nonexistent_post(self):
        """
        Удаление лайка с поста, не имеющего лайков.
        """
        response = self.client.delete(f"/api/posts/{self.post.id}/like/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Like.objects.count(), 0)
