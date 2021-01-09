from django.db import models
from login_app.models import User

class BookManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 3:
            errors['title'] = 'Title should have at least 3 characters.'

        if len(post_data['description']) < 5:
            errors['description'] = 'Description should have at least 5 characters.'

        return errors




class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    uploader = models.ForeignKey(User, related_name = 'books_uploaded', on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name = 'books_liked')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    objects = BookManager()







