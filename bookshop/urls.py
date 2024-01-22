from django.urls import path

from bookshop.views import HomePageView, PublisherView, StoreListView, StoreDetialView, StoreCreateView, \
    AuthorCreateView, AuthorListView, AuthorDetialView, BookListView, BookCreateView, BookDetialView, BookUpdateView

app_name = "bookshop"
urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("publisher/", PublisherView.as_view(), name="publisher-page"),
    path("stores/", StoreListView.as_view(), name="store-list"),
    path("stores/create", StoreCreateView.as_view(), name="store-create"),
    path("stores/<int:pk>", StoreDetialView.as_view(), name="store-detail"),
    path("authors/create", AuthorCreateView.as_view(), name="author-create"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>", AuthorDetialView.as_view(), name="author-detail"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/create", BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>", BookDetialView.as_view(), name="book-detail"),
    path("books/update/<int:pk>", BookUpdateView.as_view(), name="book-update")
]
