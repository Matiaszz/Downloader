# pylint: disable=all
import os
import yt_dlp
from django.http import JsonResponse
from django.shortcuts import render


def index(req):
    context = {'site_title': 'Início'}
    return render(req, 'downloader/pages/index.html', context=context)


def download_video(request):
    context = {'site_title': 'Download'}
    if request.method == 'POST':
        link = request.POST.get('link')

        download_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

        os.makedirs(download_folder, exist_ok=True)

        ydl_opts = {
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            return JsonResponse(
                {'status': 'success',
                 'message': 'Download concluído, '
                 'cheque sua pasta de downloads.'
                 })

        except Exception:
            return JsonResponse(
                {'status': 'error', 'message': 'Coloque um link válido'})

    return render(request, 'downloader/pages/download.html', context=context)
