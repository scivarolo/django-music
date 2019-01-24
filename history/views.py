from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Artist, Song

# Create your views here.
def index(request):
    artist_list = Artist.objects.order_by('name')
    groups = artist_list.filter(num_of_members__gt=1)
    soloists = artist_list.filter(num_of_members=1)
    context = {
        'artist_list': artist_list,
        'groups': groups,
        'soloists': soloists
    }

    return render(request, 'history/index.html', context)

def artist_detail(request, artist_id):
    # song_list = Song.objects.filter(album_id=artist_id)
    album_list = Album.objects.filter(artist_id=artist_id)
    artist = Artist.objects.get(pk=artist_id)
    print(album_list)

    for album in album_list:
        print(album.song_set.all())

    context = {
        'artist': artist,
        'albums': album_list
    }

    return render(request, 'history/artist_detail.html', context)