from django.shortcuts import render
from backend.models import LanguageDb, GenreDb, SongsDb, CombinedDb

def frontindex(request):
    genre = GenreDb.objects.all()
    lang = LanguageDb.objects.all()
    context = {'lang': lang, 'genre': genre}
    return render(request, 'home.html', context)

def frontabout(request):
    return render(request, 'about.html')

def frontcontact(request):
    return render(request, 'contact.html')

def CombinationFiltered(request, cmb_flt):
    comb = CombinedDb.objects.filter(Com_Language=cmb_flt)
    context = {'comb': comb}
    return render(request, 'comb_filtered.html', context)

def player(request):
    return render(request, 'aud/index.html')

