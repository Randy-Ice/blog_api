import uuid

from django.core.validators import MinLengthValidator
from django.db import models
from django.conf import settings
from django.db.models import ForeignKey


# Create your models here.

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, unique=True,
                             validators=[MinLengthValidator(3, message="Title must be between 3 and 100 characters")]
                             )
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", blank=True)
    IMPORTANCE_YES = 'Y'
    IMPORTANCE_NO = 'N'
    IMPORTANCE_CHOICES = (
        (IMPORTANCE_YES, 'Yes'),
        (IMPORTANCE_NO, 'No'),
    )
    important = models.CharField(max_length=1, choices=IMPORTANCE_CHOICES, default=IMPORTANCE_NO)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title



class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.title

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.author} - {self.title}"


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user__first_name', 'user__last_name']