from django.shortcuts import render,get_object_or_404
from videos.models import Playlist


def home(request):
    playlists = Playlist.objects.all()[:5]
    return render(request, "test.html", {"playlist": playlists})


def detail(request, p_id):
    playlist = get_object_or_404(Playlist, id=p_id)
    videos = playlist.videos.all()
    return render(request, "test_detail.html", {"videos": videos})

