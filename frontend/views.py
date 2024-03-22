from django.shortcuts import render
from backend.models import LanguageDb, CombinedDb, SubCombinedDb, SongsDb

def frontindex(request):
    lang = LanguageDb.objects.all()
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            lang = LanguageDb.objects.filter(Language_Name__icontains=str)
    context = {'lang': lang}
    return render(request, 'home.html', context)

def GenreFiltered(request, cmb_flt):
    comb = CombinedDb.objects.filter(Com_Language=cmb_flt)
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            comb = CombinedDb.objects.filter(Com_Genre__icontains=str)
    context = {'comb': comb}
    return render(request, 'directory/gnr_fltr.html', context)
    
def SubGenreFiltered(request, sub_flt):
    subgenre = SubCombinedDb.objects.filter(Sub_Com_Genre=sub_flt)
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            subgenre = SubCombinedDb.objects.filter(Sub_Com_Res_SubGenre__icontains=str)
    context = {'subgenre': subgenre}
    return render(request, 'directory/sbgnr_fltr.html', context)

def AudioListFiltered(request, aud_flt):
    audio = SongsDb.objects.filter(Sub_Genre=aud_flt)
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            audio = SongsDb.objects.filter(Name__icontains=str)
    context = {'audio': audio}
    return render(request, 'directory/list_fltr.html', context)

def SongFiltered(request, song_flt):
    song = SongsDb.objects.filter(Name=song_flt)
    context = {'song': song}
    return render(request, 'directory/song_fltr.html', context)


# ========================= PROFILE-PAGE ===========================================================

def frontabout(request):
    return render(request, 'main/profile.html')

def LoginPage(request):
    return render(request, 'profile/login.html')