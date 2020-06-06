from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomePage.as_view(), name='home'),
    path('detailfilm/<slug:slug>', FilmDetail.as_view(), name='detailFilm'),
    path('category/<slug:slug>', CategoryDetail.as_view(), name='detailCategory')
]