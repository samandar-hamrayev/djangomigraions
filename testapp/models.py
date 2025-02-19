from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=90, null=True)
    created_at = models.DateTimeField(auto_now=True)