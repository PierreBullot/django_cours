from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.conf import settings
from . import models

images_directory = f"{settings.BASE_DIR}/data"


def index(request):
    novels_list = models.WebNovel.objects.all()
    images_list = [{"file": novel.pk, "name": novel.name} for novel in novels_list]
    breadcrumb = [
        ("Home", "")
    ]
    context = {"breadcrumb": breadcrumb, "book_url": "/book/", "images": images_list}
    return render(request, "index.html", context)


def book(request, book_id):
    novel = get_novel_from_id(book_id)

    breadcrumb = [
        ("Home", "/"),
        (novel.name, "")
    ]

    context = {"breadcrumb": breadcrumb, "cover_url": f"/cover/{novel.pk}"}
    return render(request, "details.html", context)


def cover(request, book_id):
    novel = get_novel_from_id(book_id)

    return FileResponse(open(f"{images_directory}/{novel.cover_path}", "rb"))


def get_novel_from_id(id):
    try:
        novel = models.WebNovel.objects.get(pk=id)
    except models.WebNovel.DoesNotExist:
        novel = models.WebNovel(name="Error 404 : book not found", pk="")

    return novel