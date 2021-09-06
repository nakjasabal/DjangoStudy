from django.urls import path
from . import views

# 클래스형 뷰를 사용하기 위한 URLconf 설정. as_view() 메서드 사용.
app_name = "books"
urlpatterns = [
    path('', views.BooksModelView.as_view(), name="index"),
    path('book/', views.BookList.as_view(), name="book_list"),
    path('author/', views.AuthorList.as_view(), name="author_list"),
    path('publisher/', views.PublisherList.as_view(), name="publisher_list"),
    path('book/<int:pk>/', views.BookDetail.as_view(), name="book_detail"),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name="author_detail"),
    path('publisher/<int:pk>', views.PublisherDetail.as_view(), name="publisher_detail"),
]