from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from bookshop.forms import PublisherCreateForm, StoreCreateForm, AuthorCreateForm, BookCreateForm, BookUpdateForm
from bookshop.models import Publisher, Store, Author, Book

"""
function based views 
class based views 
    View
    generic
"""


class HomePageView(View):
    def get(self, request):
        return render(request, "bookshop/home.html")


class PublisherView(View):
    def get(self, request):
        publishers = Publisher.objects.all().order_by("-created_at")[:5]
        form = PublisherCreateForm()
        context = {
            "publishers": publishers,
            "form": form
        }
        return render(request, "bookshop/publisher.html", context=context)

    def post(self, request):
        publishers = Publisher.objects.all().order_by("-created_at")[:5]
        form = PublisherCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("bookshop:publisher-page")
        else:
            return render(request, "bookshop/publisher.html", context={
                "publishers": publishers,
                "form": form
            })

class StoreListView(ListView):
    model = Store
    context_object_name = "stores"
    template_name = "bookshop/store_list.html"

class StoreDetialView(DetailView):
    model= Store
    template_name = "bookshop/store_detail.html"
    context_object_name = "store"

class StoreCreateView(CreateView):
    model = Store
    form = StoreCreateForm
    fields = ["name", "books"]
    template_name = "bookshop/store_create.html"

class AuthorListView(ListView):
    model = Author
    context_object_name = "authors"
    template_name = "bookshop/author_list.html"

class AuthorDetialView(DetailView):
    model= Author
    template_name = "bookshop/author_detail.html"
    context_object_name = "author"

class AuthorCreateView(CreateView):
    model = Author
    form=AuthorCreateForm
    fields = ["username", "first_name", "last_name", "age"]
    template_name = "bookshop/author_create.html"

class BookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "bookshop/book_list.html"

class BookDetialView(DetailView):
    model= Book
    template_name = "bookshop/book_detail.html"
    context_object_name = "book"

class BookCreateView(CreateView):
    model = Book
    form = BookCreateForm
    fields = ["name", "rating", "price"]
    template_name = "bookshop/book_create.html"

class BookUpdateView(UpdateView):
    model = Book
    form = BookUpdateForm
    fields = ["name", "rating", "price"]
    template_name = "bookshop/book_update.html"
