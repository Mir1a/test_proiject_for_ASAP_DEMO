from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=20)
    pages = models.PositiveIntegerField(null=True, blank=True)
    cover = models.URLField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=40)

    author = models.ForeignKey(to='author.Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.published_date.year}) - {self.author}"
