import random
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate, APITestCase
from .views import UserModelViewSet
from .models import User
from mixer.backend.django import mixer

class TestUserApi(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='daniil', password='qwerty')

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_1(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        force_authenticate(request, self.user)
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_detail(self):
        user = mixer.blend(User)
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestAuthorApiClient(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='daniil', password='qwerty')

    def test_get_list(self):
        response = self.client.get('/api/user/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_list_1(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)