from django.contrib import admin
from books.models import Book, Author, Publisher

#admin 페이지에 보이도록 등록
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher) 
