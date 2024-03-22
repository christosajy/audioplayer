from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from backend.models import LanguageDb, SongsDb, GenreDb, CombinedDb, SubGenreDb, SubCombinedDb

def backindex(request):
    return render(request, 'index.html')

def AddLanguage(request):
    return render(request, 'directory/language/add_lang.html')

def SaveLanguage(request):
    if request.method == 'POST':
        lgNm = request.POST.get('langName')
        lgSt = request.POST.get('langSubt')
        lgIm = request.FILES['langImg']
        obj = LanguageDb(Language_Name=lgNm, Language_Image=lgIm, Language_Subtitle=lgSt)
        obj.save()
        return redirect(AddLanguage)
    
def DisplayLanguage(request):
    lang = LanguageDb.objects.all()
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            lang = LanguageDb.objects.filter(Language_Name__icontains=str)
    
    context = {'lang': lang}
    return render(request, 'directory/language/disp_lang.html', context)

def EditLanguage(request, langId):
    lang = LanguageDb.objects.get(id=langId)
    context = {'lang': lang}
    return render(request, 'directory/language/edit_lang.html', context)

def UpdateLanguage(request, langId):
    if request.method == 'POST':
        lgNm = request.POST.get('langName')
        lgSt = request.POST.get('langSubt')
        try:
            lgIm = request.FILES['langImg']
            file=FileSystemStorage().save(lgIm.name, lgIm)
        except MultiValueDictKeyError:
            file = LanguageDb.objects.get(id=langId).Language_Image
        LanguageDb.objects.filter(id=langId).update(Language_Name=lgNm, Language_Subtitle=lgSt, Language_Image=file)
        return redirect(DisplayLanguage)

def DeleteLanguage(request, langId):
    lang = LanguageDb.objects.filter(id=langId)
    lang.delete()
    return redirect(DeleteLanguage)


# ==================== MAIN GENRE ========================================================================

def AddGenre(request):
    return render(request, 'directory/genre/add_genre.html')

def SaveGenre(request):
    if request.method == 'POST':
        gnNm = request.POST.get('genName')
        obj = GenreDb(Genre_Name=gnNm)
        obj.save()
        return redirect(AddGenre)

def DisplayGenre(request):
    genre = GenreDb.objects.all()
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            genre = GenreDb.objects.filter(Genre_Name__icontains=str)
    context = {'genre': genre}
    return render(request, 'directory/genre/disp_genre.html', context)

def DeleteGenre(request, genreId):
    genre = GenreDb.objects.filter(id=genreId)
    genre.delete()
    messages.success(request, 'Genre deleted successfully')
    return redirect(DisplayGenre)

# ==================== SUB GENRE ========================================================================

def AddSubGenre(request):
    genre = GenreDb.objects.all()
    context = {'genre': genre}
    return render(request, 'directory/subgenre/add_subgenre.html', context)

def SaveSubGenre(request):
    if request.method == 'POST':
        SbGn = request.POST.get('SubGenName')
        SbRs = request.POST.get('SubResGen')
        obj = SubGenreDb(Sub_Genre_Name=SbGn,Res_Sub_Genre=SbRs)
        obj.save()
        return redirect(AddSubGenre)
    
def DisplaySubGenre(request):
    subgen =SubGenreDb.objects.all()
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            subgen =SubGenreDb.objects.filter(Sub_Genre_Name__icontains=str)
    context = {'subgen': subgen}
    return render(request, 'directory/subgenre/display_subgenre.html', context)

def EditSubGenre(request, subId):
    subgen =SubGenreDb.objects.get(id=subId)
    genre = GenreDb.objects.all()
    context = {'subgen': subgen, 'genre': genre}
    return render(request, 'directory/subgenre/edit_subgenre.html', context)

def UpdateSubGenre(request, subId):
    if request.method == 'POST':
        SbGn = request.POST.get('SubGenName')
        SbRs = request.POST.get('SubResGen')
        SubGenreDb.objects.filter(id=subId).update(Sub_Genre_Name=SbGn,Res_Sub_Genre=SbRs)
        return redirect(DisplaySubGenre)
 
def DeleteSubGenre(request, subId):
    subgen =SubGenreDb.objects.filter(id=subId)
    subgen.delete()
    return redirect(DisplaySubGenre)

# ==================== COMBINED SECTION =================================================================

def AddCombination(request):
    genre = GenreDb.objects.all()
    lang = LanguageDb.objects.all()
    subgen =SubGenreDb.objects.all()
    context = {'lang': lang, 'genre': genre, 'subgen': subgen}
    return render(request, 'directory/combination/add_comb.html', context)

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
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            comb = CombinedDb.objects.filter(Com_Genre__icontains=str) 
    context = {'comb': comb}
    return render(request, 'directory/combination/disp_comb.html', context)

def EditCombination(request, combId):
    genre = GenreDb.objects.all()
    lang = LanguageDb.objects.all()
    subgen =SubGenreDb.objects.all()
    comb = CombinedDb.objects.get(id=combId)
    context = {'lang': lang, 'genre': genre, 'subgen': subgen, 'comb': comb}
    return render(request, 'directory/combination/edit_comb.html', context)

def UpdateCombination(request, combId):
    if request.method == 'POST':
        cbLg = request.POST.get('CombLang')
        cbGn = request.POST.get('CombGen')
        try:
            cbIm = request.FILES['CombImg']
            file=FileSystemStorage().save(cbIm.name, cbIm)
        except MultiValueDictKeyError:
            file = CombinedDb.objects.get(id=combId).Com_Img_File
        CombinedDb.objects.filter(id=combId).update(Com_Language=cbLg, Com_Genre=cbGn, Com_Img_File=file)
        return redirect(DisplayCombination)

def DeleteCombination(request, combId):
    comb = CombinedDb.objects.filter(id=combId)
    comb.delete()
    return redirect(DisplayCombination)


#######################################################################################################

def AddSubCombination(request):
    genre = GenreDb.objects.all()
    lang = LanguageDb.objects.all()
    subgen =SubGenreDb.objects.all()
    context = {'lang': lang, 'genre': genre, 'subgen': subgen}
    return render(request, 'directory/subcombination/add_subcomb.html', context)

def SaveSubCombination(request):
    if request.method == 'POST':
        Sbcb = request.POST.get('SubCombGen')
        SbGn = request.POST.get('SubCombRes')
        SbIm = request.FILES['SubCombImg']
        obj = SubCombinedDb(Sub_Com_Genre=Sbcb, Sub_Com_Res_SubGenre=SbGn, Sub_Com_Img_File=SbIm)
        obj.save()
        return redirect(AddCombination)
    
def DisplaySubCombination(request):
    subcom = SubCombinedDb.objects.all()
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            subcom = SubCombinedDb.objects.filter(Sub_Com_Res_SubGenre__icontains=str)
    context = {'subcom': subcom}
    return render(request, 'directory/subcombination/disp_subcomb.html', context)

def EditSubCombination(request, subId):
    genre = GenreDb.objects.all()
    lang = LanguageDb.objects.all()
    subgen =SubGenreDb.objects.all()
    subcom = SubCombinedDb.objects.get(id=subId)
    context = {'lang': lang, 'genre': genre, 'subgen': subgen, 'subcom': subcom}
    return render(request, 'directory/subcombination/edit_subcomb.html', context)

def UpdateSubCombination(request, subId):
    if request.method == 'POST':
        Sbcb = request.POST.get('SubCombGen')
        SbGn = request.POST.get('SubCombRes')
        try:
            SbIm = request.FILES['SubCombImg']
            file=FileSystemStorage().save(SbIm.name, SbIm)
        except MultiValueDictKeyError:
            file = SubCombinedDb.objects.get(id=subId).Sub_Com_Img_File
        SubCombinedDb.objects.filter(id=subId).update(Sub_Com_Genre=Sbcb, Sub_Com_Res_SubGenre=SbGn, 
            Sub_Com_Img_File=file)
        return redirect(DisplaySubCombination)

def DeleteSubCombination(request, subId):
    subcom = SubCombinedDb.objects.filter(id=subId)
    subcom.delete()
    return redirect(DisplaySubCombination)


# ==================== AUDIO =====================================================================

def AddAudio(request):
    lang = LanguageDb.objects.all()
    genre = GenreDb.objects.all()
    subgenre = SubGenreDb.objects.all()
    context = {'lang': lang, 'genre': genre, 'subgenre': subgenre}
    return render(request, 'audio/add_audio.html', context)

def SaveAudio(request):
    if request.method == 'POST':
        AdNm = request.POST.get('AudName')
        AdLg = request.POST.get('AudLang')
        AdGr = request.POST.get('AudGenre')
        AdSb = request.POST.get('AudSbGnr')
        AdYr = request.POST.get('AudYear')
        AdAr = request.POST.get('AudArtist')
        AdAm = request.POST.get('AudAlbum')
        AuFl = request.FILES['AudFile']
        Imfl = request.FILES['Imgfile']
        obj = SongsDb(Name=AdNm, Language=AdLg, Genre=AdGr, Sub_Genre=AdSb, Year=AdYr, Artists=AdAr, 
            Album_or_Film=AdAm, Audio_File=AuFl, Img_File=Imfl)
        obj.save()
        return redirect(AddAudio)

def DisplayAudio(request):
    audio = SongsDb.objects.all()
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            audio = SongsDb.objects.filter(Name__icontains=str)
    context = {'audio': audio}
    return render(request, 'audio/disp_audio.html', context)

def EditAudio(request, audioId):
    lang = LanguageDb.objects.all()
    genre = GenreDb.objects.all()
    subgenre = SubGenreDb.objects.all()
    audio = SongsDb.objects.get(id=audioId)
    context = {'lang': lang, 'genre': genre, 'audio': audio, 'subgenre': subgenre}
    return render(request, 'audio/edit_audio.html', context)

def UpdateAudio(request, audioId):
    if request.method == "POST":
        AdNm = request.POST.get('EditAudName')
        AdLg = request.POST.get('EditAudLang')
        AdGr = request.POST.get('EditAudGenre')
        AdSb = request.POST.get('EditAudSbGnr')
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
        SongsDb.objects.filter(id=audioId).update(Name=AdNm, Language=AdLg, Genre=AdGr, Sub_Genre=AdSb, Year=AdYr, 
            Artists=AdAr, Album_or_Film=AdAm, Audio_File=file1, Img_File=file2)
        return redirect(DisplayAudio)      

def DeleteAudio(request, audioId):
    audio = SongsDb.objects.filter(id=audioId)
    audio.delete()
    return redirect(DisplayAudio)