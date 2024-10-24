# pylint: disable=all
from django.urls import path
from .views import index, download_video

app_name = 'downloader'

urlpatterns = [
    path('', index, name='index'),
    path('download/', download_video, name='download_video'),
]
