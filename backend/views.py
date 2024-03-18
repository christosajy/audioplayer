from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from backend.models import LanguageDb, SongsDb, GenreDb, CombinedDb

def backindex(request):
    return render(request, 'index.html')

def AddLanguageAndGenre(request):
    return render(request, 'directory/add_lang_genre.html')

def SaveLanguage(request):
    if request.method == 'POST':
        lgNm = request.POST.get('langName')
        lgSt = request.POST.get('langSubt')
        lgIm = request.FILES['langImg']
        obj = LanguageDb(Language_Name=lgNm, Language_Image=lgIm, Language_Subtitle=lgSt)
        obj.save()
        return redirect(AddLanguageAndGenre)
    
def DisplayLanguage(request):
    lang = LanguageDb.objects.all()
    context = {'lang': lang}
    return render(request, 'directory/disp_lang.html', context)

def DeleteLanguage(request, langId):
    lang = LanguageDb.objects.filter(id=langId)
    lang.delete()
    return redirect(DeleteLanguage)


# ==================== AUDIO =====================================================================

def SaveGenre(request):
    if request.method == 'POST':
        gnNm = request.POST.get('genName')
        gnSt = request.POST.get('genSbtl')
        obj = GenreDb(Genre_Name=gnNm, Genre_Subtitle=gnSt)
        obj.save()
        return redirect(AddLanguageAndGenre)

def DisplayGenre(request):
    genre = GenreDb.objects.all()
    context = {'genre': genre}
    return render(request, 'directory/disp_genre.html', context)

def EditGenre(request, genreId):
    genre = GenreDb.objects.get(id=genreId)
    context = {'genre': genre}
    return render(request, 'directory/edit_genre.html', context)

def UpdateGenre(request, genreId):
    if request.method == 'POST':
        gnNm = request.POST.get('EditGenName')
        gnSt = request.POST.get('EditGenSbtl')
        GenreDb.objects.filter(id=genreId).update(Genre_Name=gnNm, Genre_Subtitle=gnSt)
        return redirect(DisplayGenre)

def DeleteGenre(request, genreId):
    genre = GenreDb.objects.filter(id=genreId)
    genre.delete()
    messages.success(request, 'Genre deleted successfully')
    return redirect(DisplayGenre)
    
# ==================== COMBINED SECTION ==========================================================

def AddCombination(request):
    genre = GenreDb.objects.all()
    lang = LanguageDb.objects.all()
    context = {'lang': lang, 'genre': genre}
    return render(request, 'directory/add_comb.html', context)

def SaveCombination(request):
    if request.method == 'POST':
        cbLg = request.POST.get('CombLang')
        cbGn = request.POST.get('CombGen')
        cbIm = request.FILES['CombImg']
        obj = CombinedDb(Com_Language=cbLg, Com_Genre=cbGn, Com_Img_File=cbIm)
        obj.save()
        return redirect(AddCombination)

def DisplayCombination(request):
    comb = CombinedDb.objects.all()
    context = {'comb': comb}
    return render(request, 'directory/disp_comb.html', context)

def DeleteCombination(request, combId):
    comb = CombinedDb.objects.filter(id=combId)
    comb.delete()
    return redirect(DisplayCombination)

# ==================== AUDIO =====================================================================

def AddAudio(request):
    lang = LanguageDb.objects.all()
    genre = GenreDb.objects.all()
    context = {'lang': lang, 'genre': genre}
    return render(request, 'audio/add_audio.html', context)

def SaveAudio(request):
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
        return redirect(AddAudio)

def DisplayAudio(request):
    audio = SongsDb.objects.all()
    context = {'audio': audio}
    return render(request, 'audio/disp_audio.html', context)

def EditAudio(request, audioId):
    lang = LanguageDb.objects.all()
    genre = GenreDb.objects.all()
    audio = SongsDb.objects.get(id=audioId)
    context = {'lang': lang, 'genre': genre, 'audio': audio}
    return render(request, 'audio/edit_audio.html', context)

def UpdateAudio(request, audioId):
    if request.method == "POST":
        AdNm = request.POST.get('EditAudName')
        AdLg = request.POST.get('EditAudLang')
        AdGr = request.POST.get('EditAudGenre')
        AdYr = request.POST.get('EditAudYear')
        AdAr = request.POST.get('EditAudArtist')
        AdAm = request.POST.get('EditAudAlbum')
        try:
            AuFl = request.FILES['EditAudFile']
            file1 = FileSystemStorage().save(AuFl.name, AuFl)
            Imfl = request.FILES['EditImgfile']
            file2 = FileSystemStorage().save(Imfl.name, Imfl)
        except MultiValueDictKeyError:
            file1 = SongsDb.objects.get(id=audioId).Audio_File
            file2 = SongsDb.objects.get(id=audioId).Img_File
        SongsDb.objects.filter(id=audioId).update(Name=AdNm, Language=AdLg, Genre=AdGr, Year=AdYr, Artists=AdAr, 
                Album_or_Film=AdAm, Audio_File=file1, Img_File=file2)
        return redirect(DisplayAudio)      

def DeleteAudio(request, audioId):
    audio = SongsDb.objects.filter(id=audioId)
    audio.delete()
    return redirect(DisplayAudio)