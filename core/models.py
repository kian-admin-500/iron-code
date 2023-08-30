from django.db import models

# Create your models here.

class AdminTable(models.Model):
    username = models.TextField(null=True , blank=False , max_length=20)
    password = models.TextField(null=True , blank=False , max_length=20)

    def __str__(self):
        return self.username
