from django.db import models # imports Django's model module[part of Django's ORM (Object-Relational Mapping)]. ORM allows you to interact with the database in an object-oriented way.
import uuid #generate unique identifiers; uuid4 generates a random UUID.

class Snippet(models.Model): #model class -> inherits from models.Model; linked to a database table.
    code = models.TextField() # text field for storing code snippets
    created_at = models.DateTimeField(auto_now_add=True) # record the date and time when a new model instance is created and saved to the database
    unique = models.SlugField(default=uuid.uuid4, unique=True, editable=False)
    # sets the default value for the field to a unique UUID (each Snippet -> unique); 
    # called without parentheses = a new UUID generated each time a new record is created, 
    # rather than using the same UUID for all instances.
    # unique=True = no two snippets can have the same name(uniqueness at the database level).
    # editable=False: prevents editing via Django admin or forms(URLs remain the same after creation, name cannot be changed).

