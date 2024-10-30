from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from .models import Book
from author.models import Author


class BookViewSetTest(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name='Test',
            last_name='Author',
            date_of_birth='1980-01-01',
            biography='Biography of test author'
        )
        self.book_data = {
            'title': 'Test Book',
            'published_date': '2024-01-01',
            'isbn': '1234567890',
            'pages': 300,
            'cover': 'http://example.com/cover.jpg',
            'language': 'English',
            'author_id': self.author.id,
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        response = self.client.post(reverse('book-list'), self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        update_data = self.book_data.copy()
        update_data['title'] = 'Updated Test Book'
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.put(url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
