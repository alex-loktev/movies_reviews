from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import *


class HomePage(ListView):
    """List all film in home page"""

    model = Film
    context_object_name = 'films'
    template_name = 'main/home.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class FilmDetail(View):
    """Detail information about film and realisation of comments"""

    def get(self, request, slug):
        film = Film.objects.get(slug=slug)
        form = ComentCreateForm()
        return render(request, 'main/detailFilm.html', {'film': film, 'form': form})

    def post(self, request, slug):
        film = Film.objects.get(slug=slug)
        form = ComentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            film.rating = (film.rating * film.number_of_comments + comment.rating)/(film.number_of_comments + 1)
            film.number_of_comments = int(film.number_of_comments) + 1
            film.save()
            print(film.number_of_comments)
            comment.film = film
            comment.save()
            return redirect('detailFilm', slug=slug)
        return render(request, 'main/detailFilm.html', {'film': film, 'form': form})


class CategoryDetail(DetailView):
    """Films with the selected category"""

    model = Category
    context_object_name = 'category'
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Film.objects.all().filter(categories=context['category'])
        context['categories'] = Category.objects.all()
        return context



