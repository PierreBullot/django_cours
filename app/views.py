from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.conf import settings
from . import models

images_directory = f"{settings.BASE_DIR}/data"


def index(request):
    novels_list = models.WebNovel.objects.all()
    breadcrumb = [
        ("Home", "")
    ]
    context = {"breadcrumb": breadcrumb, "book_url": "/book/", "novels": novels_list}
    return render(request, "index.html", context)


def book(request, book_name):
    novel = get_novel_from_name(book_name)
    if novel is None:
        return render(request, "404.html")

    breadcrumb = [
        ("Home", "/"),
        (novel.name, "")
    ]

    context = {"breadcrumb": breadcrumb, "cover_url": f"/cover/{novel.name}"}
    return render(request, "details.html", context)


def cover(request, book_name):
    novel = get_novel_from_name(book_name)

    return FileResponse(open(f"{images_directory}/{novel.cover_path}", "rb"))


def get_novel_from_name(name):
    try:
        novel = models.WebNovel.objects.get(name=name)
    except models.WebNovel.DoesNotExist:
        novel = None

    return novel