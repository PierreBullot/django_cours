from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.conf import settings
import os

images_directory = f"{settings.BASE_DIR}/data"


def index(request):
    images_list = [{"file": image, "name": image.split(".")[0]} for image in os.listdir(images_directory)]
    breadcrumb = [
        ("Home", "")
    ]
    context = {"breadcrumb": breadcrumb, "book_url": "/book/", "images": images_list}
    return render(request, "index.html", context)


def book(request, path):
    breadcrumb = [
        ("Home", "/"),
        (path.split(".")[0], "")
    ]

    context = {"breadcrumb": breadcrumb, "cover_url": f"/cover/{path}"}
    return render(request, "details.html", context)


def cover(request, path):
    return FileResponse(open(f"{images_directory}/{path}", "rb"))
