from django.db import models
# from django.contrib.auth.models import User


class HomePageContent(models.Model):

    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.header
