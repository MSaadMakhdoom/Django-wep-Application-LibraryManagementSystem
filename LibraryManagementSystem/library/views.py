# library/views.py

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Borrow


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # check if user is superuser
            if user.is_superuser:
                return redirect('admin')
            else:
                return redirect('home')
        else:
            error = "Invalid username or password"
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')
    
@login_required(login_url='/login/')
def admin_view(request):
        # count total books
    total_books = Book.objects.count()
    # count total authors
    total_authors = Author.objects.count()
    print("Total Books: ", total_books)
    print("Total Authors: ", total_authors)
    return render(request, 'admin.html', {'total_books': total_books, 'total_authors': total_authors})

# edit the book
@login_required(login_url='/login/')
def edit_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.description = request.POST['description']
        book.ISBN = request.POST['ISBN']
        book.Genre = request.POST['Genre']
        book.cover_image = request.POST['cover_image']
        book.save()
        return redirect('all_books')
    else:
        return render(request, 'edit_book.html', {'book': book})
    
# edit the author
@login_required(login_url='/login/')
def edit_author_view(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        author.first_name = request.POST['first_name']
        author.last_name = request.POST['last_name']
        author.bio = request.POST['bio']
        author.image = request.POST['image']
        author.save()
        return redirect('all_authors')
    else:
        return render(request, 'edit_author.html', {'author': author})
    
# Delete the author
@login_required(login_url='/login/')
def delete_author_view(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('all_authors')
    else:
        return render(request, 'delete_author.html', {'author': author})




# add the book
@login_required(login_url='/login/')
def add_book_view(request):
    if request.method == 'POST':
        book = Book()
        book.title = request.POST['title']
        print("Add new Book ",request.POST['author'])
        authors = Author.objects.get(id=request.POST['author'])
        book.author = authors

        book.description = request.POST['description']
        book.ISBN = request.POST['ISBN']
        book.Genre = request.POST['Genre']
        book.cover_image = request.POST['cover_image']
        book.save()
        return redirect('all_books')
    else:
        authors = Author.objects.all()
        return render(request, 'add_book.html', {'authors': authors})
    
# add the author
@login_required(login_url='/login/')
def add_author_view(request):
    if request.method == 'POST':
        author = Author()
        author.first_name = request.POST['first_name']
        author.last_name = request.POST['last_name']
        author.bio = request.POST['bio']
        author.image = request.POST['image']
        author.save()
        return redirect('all_authors')
    else:
        
        return render(request, 'add_author.html')
    


# delete the book
@login_required(login_url='/login/')
def delete_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('all_books')
    else:
        return render(request, 'delete_book.html', {'book': book})
    



def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# @login_required(login_url='/login/')
def home_view(request):
    # count total books
    total_books = Book.objects.count()
    # count total authors
    total_authors = Author.objects.count()
    
    return render(request, 'home.html', {'total_books': total_books, 'total_authors': total_authors})

@login_required(login_url='/login/')
def all_books_view(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})

@login_required(login_url='/login/')
def book_detail_view(request, book_id):
    print("Book ID: ", book_id)
    book = Book.objects.get(id=book_id)
    # book = Book.objects.filter(id=book_id)
    print("Book Detail: ", book)

    return render(request, 'books_detail.html', {'book': book})

@login_required(login_url='/login/')
def all_authors_view(request):
    authors = Author.objects.all()
    return render(request, 'all_authors.html', {'authors': authors})

@login_required(login_url='/login/')
def author_detail_view(request, author_id):
    author = Author.objects.get(id=author_id)
    books= Book.objects.filter(author=author)
    print("Author: ", author.first_name)
    print("Book: ", books)

    return render(request, 'author_detail.html', {'author': author, 'books': books})


@login_required(login_url='/login/')
def my_books_view(request):
    print("User: ", request.user)
    user_borrows = Borrow.objects.filter(user=request.user)
    print("User borrows: ", user_borrows)
    return render(request, 'my_books.html', {'user_borrows': user_borrows})
