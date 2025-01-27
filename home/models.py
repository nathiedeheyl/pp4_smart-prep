from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HomePageContent(models.Model):
    header = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.header