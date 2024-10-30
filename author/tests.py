from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Author
from django.utils import timezone


class AuthorViewSetTest(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth=timezone.now().date(),
            biography='Test biography'
        )

        self.author_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'date_of_birth': timezone.now().date(),
            'biography': 'New biography'
        }

        self.update_data = {
            'first_name': 'John Updated',
            'last_name': 'Doe Updated',
            'date_of_birth': timezone.now().date(),
            'biography': 'Updated biography'
        }

    def test_list_authors(self):
        url = reverse('author-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author(self):
        url = reverse('author-list')
        response = self.client.post(url, self.author_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)
        self.assertEqual(Author.objects.get(first_name='Jane').last_name, 'Smith')

    def test_retrieve_author(self):
        url = reverse('author-detail', kwargs={'pk': self.author.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.author.first_name)

    def test_update_author(self):
        url = reverse('author-detail', kwargs={'pk': self.author.pk})
        response = self.client.put(url, self.update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.author.refresh_from_db()
        self.assertEqual(self.author.first_name, 'John Updated')
        self.assertEqual(self.author.biography, 'Updated biography')

    def test_delete_author(self):
        url = reverse('author-detail', kwargs={'pk': self.author.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 0)
