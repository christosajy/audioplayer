from django.shortcuts import render
from backend.models import LanguageDb, GenreDb, CombinedDb, SubCombinedDb, SongsDb

def frontindex(request):
    genre = GenreDb.objects.all()
    lang = LanguageDb.objects.all()
    context = {'lang': lang, 'genre': genre}
    return render(request, 'home.html', context)

def frontabout(request):
    return render(request, 'about.html')

def frontcontact(request):
    return render(request, 'contact.html')

def GenreFiltered(request, cmb_flt):
    comb = CombinedDb.objects.filter(Com_Language=cmb_flt)
    context = {'comb': comb}
    return render(request, 'gnr_fltr/gnr_fltr.html', context)
    
def SubGenreFiltered(request, sub_flt):
    subgenre = SubCombinedDb.objects.filter(Sub_Com_Genre=sub_flt)
    context = {'subgenre': subgenre}
    return render(request, 'sbgnr_fltr/sbgnr_fltr.html', context)

def AudioListFiltered(request, aud_flt):
    audio = SongsDb.objects.filter(Sub_Genre=aud_flt)
    context = {'audio': audio}
    return render(request, 'list_fltr/list_fltr.html', context)

def SongFiltered(request, song_flt):
    song = SongsDb.objects.filter(Name=song_flt)
    context = {'song': song}
    return render(request, 'song_fltr/song_fltr.html', context)

