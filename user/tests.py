from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from user.models import User
from rest_framework.test import APIClient


class UserViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )

        self.user_data = {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'newuser@example.com'
        }

        self.update_data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com'
        }

    def test_list_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        url = reverse('user-list')
        response = self.client.post(url, {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'newuser@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }, format='json')
        print("Create user response:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='newuser').email, 'newuser@example.com')

    def test_retrieve_user(self):
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_update_user(self):
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.patch(url, {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'first_name': 'Updated',
            'last_name': 'User'
        }, format='json')
        print("Update user response:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.email, 'updateduser@example.com')

    def test_delete_user(self):
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
