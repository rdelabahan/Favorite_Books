from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book
from login_app.models import User



def index(request):
    context = {
        'books': Book.objects.all(),
        'this_user': User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'book_index.html',context)

def create(request):
    errors = Book.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/books')

    else:
        uploader = User.objects.get(id = request.session['user_id'])
        this_book = Book.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            uploader = uploader,
        )
        this_book.users_who_like.add(uploader)
        return redirect('/books')

def display_book(request, book_id):
    context = {
        'book': Book.objects.get(id = book_id),
        'this_user': User.objects.get(id = request.session['user_id'])
    }
    return render(request,'book.html',context)

def update(request, book_id):
    errors = Book.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f'/books/{book_id}')
    else:
        this_book = Book.objects.get(id = book_id)
        this_book.title = request.POST['title']
        this_book.description = request.POST['description']
        this_book.save()
        return redirect('/books')

def delete(request, book_id):
    this_book = Book.objects.get(id = book_id)
    this_book.delete()
    return redirect('/books')

def unfavorite(request, book_id):
    this_book = Book.objects.get(id = book_id)
    this_user = User.objects.get(id = request.session['user_id'])
    this_book.users_who_like.remove(this_user)
    return redirect(f'/books/{book_id}')

def favorite(request, book_id):
    this_book = Book.objects.get(id = book_id)
    this_user = User.objects.get(id = request.session['user_id'])
    this_book.users_who_like.add(this_user)
    return redirect(f'/books/{book_id}')