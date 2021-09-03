from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    # N:N관계. 저자와 책의 관계. 저자는 여러권의 책을 쓸수있다.
    authors = models.ManyToManyField('Author') 
    # 1:N관계. 출판사와 책의 관계. 책은 한 출판사에서만 발행된다. 
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE) 
    publicaton_date = models.DateField

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    salutation = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name



