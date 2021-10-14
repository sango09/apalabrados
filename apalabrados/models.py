"""Model of apalabrados."""

# Django
from django.db import models


class Numbers(models.Model):
    """Model for storing only numbers."""
    number = models.IntegerField()
    accumulated = models.IntegerField()


class Texts(models.Model):
    """Model for storing only text with initial and final characters."""
    text = models.TextField()
    initial = models.CharField(max_length=5)
    final = models.CharField(max_length=5)


class Characters(models.Model):
    """Model for storing only characters from texts."""
    character = models.CharField(max_length=10)
