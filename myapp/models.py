from django.db import models


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comment = models.TextField(max_length=9999)

    def __str__(self):
        return self.name
