# Profile REST API
profile REST API

to set push changes to github using PAT
git remote set-url origin https://<YOUR_TOKEN>@github.com/codecasualty/djangoApi.git


There will be some binary files which should not be commited,python binary files, thus we add in git ignore files

Model in Django
A model in Django is a Python class that subclasses django.db.models.Model and represents a table in your database. Each attribute of the model class represents a field of the table or a relationship between tables. The model is the single, definitive source of truth about your data. It contains the essential fields and behaviors of the data you’re storing. Django follows the DRY Principle, so the model is also responsible for defining the database schema (fields and relationships), with migrations generated based on changes in the model to keep the database in sync.

Example of a Django Model:
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
```

Model Manager in Django
A model manager is an interface through which Django models interact with the database. It is the bridge between your Django model objects and the database. Managers are Django's way to perform database queries. Each Django model has at least one manager, and custom managers can be created to extend or modify the default manager behavior.

```python
class AvailableBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()  # Default manager.
    available_books = AvailableBookManager()  # Custom manager.

    def __str__(self):
        return self.title
```
In this example, Book.objects would use the default manager, providing access to all books, whereas Book.available_books would use the AvailableBookManager, which filters the books to return only those that are available.


Django admin allows use to create adminstrative access to our database.This helps us to inspect the database, see models and modify them
to create a superuser we user django cli we type command
python manage.py createsuperuser
and enter the required details and then it will help us in accessing the database using this super_user


helper class to create our api endpoints
apiview
viewset

apiview most basic , describe logic to make our endpoints

uses standard http methods for functions
like get, to get one or more items
post to post an item
put to update and item
patch to partially update an item
delete to delete an items

give most control over logic, we can call other apis, helps in working with local files


when to use apiviews
1) need full control over the logic like updating multiple datasources in one call
processing files and rendering a synchronous response
calling other api/services in same requests
when we need access to local files or data 
