from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
