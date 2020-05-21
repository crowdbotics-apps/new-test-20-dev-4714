from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    r4 = models.BigIntegerField(null=True, blank=True,)
    r2 = models.BigIntegerField(null=True, blank=True,)
    r5 = models.BigIntegerField(null=True, blank=True,)
    r6 = models.BigIntegerField(null=True, blank=True,)
    r7 = models.BigIntegerField(null=True, blank=True,)
    r8 = models.BigIntegerField(null=True, blank=True,)
    r9 = models.BigIntegerField(null=True, blank=True,)
    r10 = models.BigIntegerField(null=True, blank=True,)
    r123 = models.BigIntegerField(null=True, blank=True,)

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
    r1 = models.BigIntegerField(null=True, blank=True,)
    r2 = models.BigIntegerField(null=True, blank=True,)

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
