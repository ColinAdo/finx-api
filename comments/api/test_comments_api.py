from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from .serializers import CommentSerializer
from comments.models import Comment
from posts.models import Post

# Comment api test case
class TestComment(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create(
            username='testuser',
            email='testuser@gmail.com',
            password='password',
        )

        cls.post = Post.objects.create(
            author=cls.user,
            caption='test post',
        )

        cls.comment = Comment.objects.create(
            owner=cls.user,
            post=cls.post,
            comment='test comment',
        )
        cls.access_token = AccessToken.for_user(cls.user)
    
    def test_create_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse('comments-list')
        data = {
            "owner": self.user.id,
            "post": self.post.id,
            "comment": 'test comment'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_get_all_comments(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse('comments-list')
        response = self.client.get(url, format='json')

        queryset = Comment.objects.all()
        expected_data = CommentSerializer(queryset, many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertEqual(len(response.data), 1)
        self.assertContains(response, str(self.user.id))

    def test_retrieve_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse('comments-detail', kwargs={'pk': self.comment.id})
        response = self.client.get(url, format='json')

        object = Comment.objects.get(id=self.comment.id)
        expected_data = CommentSerializer(object).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertContains(response, self.comment.comment)

    def test_update_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse('comments-detail', kwargs={'pk': self.comment.id})
        data = {
            "owner": self.user.id,
            "post": self.post.id,
            "comment": "updated comment"
        }
        response = self.client.put(url, data, format='json')
        self.comment.refresh_from_db()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.comment.comment, "updated comment")

    def test_delete_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse('comments-detail', kwargs={'pk': self.comment.id})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)
