from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.conf import settings
from django.views.generic import ListView, DetailView, CreateView
from . import models
from . import forms

images_directory = f"{settings.BASE_DIR}/data"


def cover(request, book_name):
    novel = get_novel_from_name(book_name)

    return FileResponse(novel.cover)


def get_novel_from_name(name):
    try:
        novel = models.WebNovel.objects.get(name=name)
    except models.WebNovel.DoesNotExist:
        novel = None

    return novel


class BookList(ListView):
    template_name = 'index.html'
    model = models.WebNovel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_book_form = forms.BookForm()
        context["form"] = new_book_form
        context["book_url"] = "/book/"
        context["breadcrumb"] = [
            ("Home", "")
        ]

        return context


class BookDetail(DetailView):
    template_name = 'details.html'
    model = models.WebNovel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        novel = self.object
        context["breadcrumb"] = [
            ("Home", "/"),
            (novel.name, "")
        ]
        context["cover_url"] = f"/cover/{novel.name}"

        return context


class CreateBook(CreateView):
    template_name = 'create.html'
    form_class = forms.BookForm
