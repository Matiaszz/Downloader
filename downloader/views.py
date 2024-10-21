from django.shortcuts import render


def index(req):
    return render(req, 'downloader/pages/index.html')


def search(req):
    return render(req, 'downloader/pages/test.html')
