from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('books/', all_books_view, name='all_books'),
    path('books/<int:book_id>/', book_detail_view, name='book_detail'),
    path('authors/', all_authors_view, name='all_authors'),
    path('authors/<int:author_id>/', author_detail_view, name='author_detail'),
    path('my-books/', my_books_view, name='my_books'),
    path('adminuser/', admin_view, name='admin'),
    #   edit book
    path('books/<int:book_id>/edit/', edit_book_view, name='edit_book'),
    #   delete book
    path('books/<int:book_id>/delete/', delete_book_view, name='delete_book'),
    # edit author
    path('authors/<int:author_id>/edit/', edit_author_view, name='edit_author'),
    # delete author
    path('authors/<int:author_id>/delete/', delete_author_view, name='delete_author'),
    

    # add book
    path('books/add/', add_book_view, name='add_book'),
    # add author
    path('authors/add/', add_author_view, name='add_author'),


    
]
