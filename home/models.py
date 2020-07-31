from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    number = models.BigIntegerField(null=True, blank=True,)
    tests = models.ForeignKey(
        "home.CustomText",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_tests",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    user2 = models.ForeignKey(
        "home.CustomText",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="homepage_user2",
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
