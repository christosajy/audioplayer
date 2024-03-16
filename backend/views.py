from django.shortcuts import render, redirect
from backend.models import LanguageDb, SongsDb, GenreDb

def backindex(request):
    return render(request, 'index.html')

def addlang(request):
    return render(request, 'lang/add_lang.html')

def savelang(request):
    if request.method == 'POST':
        lgNm = request.POST.get('langName')
        lgSt = request.POST.get('langSubt')
        lgIm = request.FILES['langImg']
        obj = LanguageDb(Language_Name=lgNm, Language_Image=lgIm, Language_Subtitle=lgSt)
        obj.save()
        return redirect(addlang)
    
def displaylang(request):
    lang = LanguageDb.objects.all()
    context = {'lang': lang}
    return render(request, 'lang/disp_lang.html', context)

def deletelang(request, langId):
    lang = LanguageDb.objects.filter(id=langId)
    lang.delete()
    return redirect(displaylang)


# ==================== AUDIO =====================================================================

def add_genre(request):
    return render(request, 'genre/addgenre.html')

def save_genre(request):
    if request.method == 'POST':
        gnNm = request.POST.get('genName')
        gnSt = request.POST.get('genSbtl')
        obj = GenreDb(Genre_Name=gnNm, Genre_Subtitle=gnSt)
        obj.save()
        return redirect(add_genre)

def disp_genre(request):
    genre = GenreDb.objects.all()
    context = {'genre': genre}
    return render(request, 'genre/disp_genre.html', context)


def delete_genre(request, genreId):
    genre = GenreDb.objects.filter(id=genreId)
    genre.delete()
    return redirect(disp_genre)
    


# ==================== AUDIO =====================================================================

def addaudio(request):
    lang = LanguageDb.objects.all()
    genre = GenreDb.objects.all()
    context = {'lang': lang, 'genre': genre}
    return render(request, 'audio/add_audio.html', context)

def saveaudio(request):
    if request.method == 'POST':
        AdNm = request.POST.get('AudName')
        AdLg = request.POST.get('AudLang')
        AdGr = request.POST.get('AudGenre')
        AdYr = request.POST.get('AudYear')
        AdAr = request.POST.get('AudArtist')
        AdAm = request.POST.get('AudAlbum')
        AuFl = request.FILES['AudFile']
        Imfl = request.FILES['Imgfile']
        obj = SongsDb(Name=AdNm, Language=AdLg, Genre=AdGr, Year=AdYr, Artists=AdAr, Album_or_Film=AdAm, 
            Audio_File=AuFl, Img_File=Imfl)
        obj.save()
        return redirect(addaudio)

def displayaudio(request):
    audio = SongsDb.objects.all()
    context = {'audio': audio}
    return render(request, 'audio/disp_audio.html', context)

def editaudio(request, audioId):
    lang = LanguageDb.objects.all()
    genre = GenreDb.objects.all()
    audio = SongsDb.objects.get(id=audioId)
    context = {'lang': lang, 'genre': genre, 'audio': audio}
    return render(request, 'audio/edit_audio.html', context)

def audiodelete(request, audioId):
    audio = SongsDb.objects.filter(id=audioId)
    audio.delete()
    return redirect(displayaudio)