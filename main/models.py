from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Film(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, db_index=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    release = models.DateTimeField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=50, blank=True)
    producer = models.CharField(max_length=124, blank=True)
    budget = models.BigIntegerField(default=1000000, blank=True)
    number_of_comments = models.IntegerField(default=100)
    categories = models.ManyToManyField('Category', related_name='films', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detailFilm', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('-rating',)


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, db_index=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detailCategory', kwargs={'slug': self.slug})


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    rating = models.IntegerField(default=10)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)