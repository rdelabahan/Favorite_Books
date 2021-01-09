from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('<int:book_id>', views.display_book),
    path('<int:book_id>/update', views.update),
    path('<int:book_id>/delete', views.delete),
    path('<int:book_id>/unfavorite', views.unfavorite),
    path('<int:book_id>/favorite', views.favorite),
]