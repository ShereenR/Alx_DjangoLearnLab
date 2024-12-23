from django.db import models

# Create your models here.
class Author(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title= models.CharField(max_length=50)
    author= models.ForeignKey(Author, on_delete=models.CASCADE,related_name='created_by')

class Library(models.Model):
    name= models.CharField(max_length=50)
    books=models.ManyToManyField(Book, on_delete=models.CASCADE ,related_name= 'content')

class Librarian(models.Model):
    name= models.CharField(max_length=50)
    library= models.OneToOneField(Library ,on_delete=models.CASCADE,related_name='keeper')