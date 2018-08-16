from django.db import models
from localflavor.us.models import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=512)

    class Meta:
            verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=512)
    author = models.CharField(max_length=256)
    categories = models.ManyToManyField(Category, related_name='books')
    cover_image = models.ImageField(upload_to='covers')
    link = models.URLField(max_length=512, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    position = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Resource(models.Model):
    title = models.CharField(max_length=512)
    short_description = models.CharField(max_length=2048, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=512, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    position = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
