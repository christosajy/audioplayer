from django.shortcuts import render
from backend.models import LanguageDb, GenreDb, SongsDb

def frontindex(request):
    genre = GenreDb.objects.all()
    lang = LanguageDb.objects.all()
    context = {'lang': lang, 'genre': genre}
    return render(request, 'home.html', context)

def frontabout(request):
    return render(request, 'about.html')

def frontcontact(request):
    return render(request, 'contact.html')

def audiolist(request, sng_flt):
    audio = SongsDb.objects.filter(Language=sng_flt)
    context = {'audio': audio}
    return render(request, 'lst/index.html', context)

def player(request):
    return render(request, 'aud/index.html')

