from django.urls import path, include
from .views import *

urlpatterns = [
    # as.view() - класс view, если его там нет то пишем просто .view
    path('Movie/', MovieListView.as_view()),
    path('movie/<int:pk>', MovieDetail.as_view()),
    path('review/', ReviewCreateView.as_view()),
    path('create/movie/', CreateMovieView.as_view())
]
