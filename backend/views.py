from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from backend.models import LanguageDb, SongsDb, GenreDb, SubGenreDb
from frontend.models import UsersDb

def backindex(request):
    return render(request, 'index.html')

def AddLanguage(request):
    return render(request, 'directory/language/add_lang.html')

def SaveLanguage(request):
    if request.method == 'POST':
        lgNm = request.POST.get('langName')
        lgSt = request.POST.get('langSubt')
        lgIm = request.FILES['langImg']
        if LanguageDb.objects.filter(Lang_Name=lgNm).exists():
            messages.error(request, 'Existing Language')
            return redirect(AddLanguage)
        else:
            obj = LanguageDb(Lang_Name=lgNm, Lang_Img=lgIm, Lang_Sbtl=lgSt)
            obj.save()
            messages.success(request, 'Upload Successfull')
            return redirect(AddLanguage)
    
def DisplayLanguage(request):
    lang = LanguageDb.objects.all()
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            lang = LanguageDb.objects.filter(Lang_Name__icontains=str)
    
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
        LanguageDb.objects.filter(id=langId).update(Lang_Name=lgNm, Lang_Sbtl=lgSt, Lang_Img=file)
        messages.success(request, 'Updation Successfull')
        return redirect(DisplayLanguage)

def DeleteLanguage(request, langId):
    lang = LanguageDb.objects.filter(id=langId)
    lang.delete()
    messages.success(request, 'Removal Successfull')
    return redirect(DisplayLanguage)


# ==================== MAIN GENRE ========================================================================

def AddGenre(request):
    lang = LanguageDb.objects.all()
    context = {'lang': lang}
    return render(request, 'directory/genre/add_genre.html', context)

def SaveGenre(request):
    if request.method == 'POST':
        lan = request.POST.get('lang')
        gnr = request.POST.get('genre')
        img = request.FILES['image']
        obj = GenreDb(LangName=lan, GenreName=gnr, GenreImg=img)
        obj.save()
        messages.success(request, 'Upload Successful')
        return redirect(AddGenre)

def DisplayGenre(request):
    genre = GenreDb.objects.all()
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            genre = GenreDb.objects.filter(LangName__icontains=str)
    context = {'genre': genre}
    return render(request, 'directory/genre/disp_genre.html', context)

def EditGenre(request, genreId):
    lang = LanguageDb.objects.all()
    genre = GenreDb.objects.get(id=genreId)
    context = {'genre': genre, 'lang': lang}
    return render(request, 'directory/genre/edit_genre.html', context)

def UpdateGenre(request, genreId):
    if request.method == 'POST':
        lan = request.POST.get('lang')
        gnr = request.POST.get('genre')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = GenreDb.objects.get(id=genreId).GenreImg
        GenreDb.objects.filter(id=genreId).update(LangName=lan, GenreName=gnr, GenreImg=file)
        messages.success(request, 'Updation Successful')
        return redirect(DisplayGenre)
        

def DeleteGenre(request, genreId):
    genre = GenreDb.objects.filter(id=genreId)
    genre.delete()
    messages.success(request, 'Removal Successful')
    return redirect(DisplayGenre)

# ==================== SUB GENRE ========================================================================

def AddSubGenre(request):
    genre = GenreDb.objects.all()
    context = {'genre': genre}
    return render(request, 'directory/subgenre/add_subgenre.html', context)

def SaveSubGenre(request):
    if request.method == 'POST':
        gnr = request.POST.get('genre')
        sub = request.POST.get('subgenre')
        img = request.FILES['image']
        if SubGenreDb.objects.filter(SubName=sub).exists():
            messages.error(request, 'Already Existing')
            return redirect(AddSubGenre)
        else:
            obj = SubGenreDb(GenreName=gnr,SubName=sub, SubImg=img)
            obj.save()
            messages.success(request, 'Upload Successfull')
            return redirect(AddSubGenre)
    
def DisplaySubGenre(request):
    subgen =SubGenreDb.objects.all()
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            subgen =SubGenreDb.objects.filter(SubName__icontains=str)
    context = {'subgen': subgen}
    return render(request, 'directory/subgenre/display_subgenre.html', context)

def EditSubGenre(request, subId):
    subgen =SubGenreDb.objects.get(id=subId)
    genre = GenreDb.objects.all()
    context = {'subgen': subgen, 'genre': genre}
    return render(request, 'directory/subgenre/edit_subgenre.html', context)

def UpdateSubGenre(request, subId):
    if request.method == 'POST':
        gnr = request.POST.get('genre')
        sub = request.POST.get('subgenre')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = SubGenreDb.objects.get(id=subId).SubImg
        SubGenreDb.objects.filter(id=subId).update(GenreName=gnr,SubName=sub, SubImg=file)
        messages.success(request, 'Updation Successfully')
        return redirect(DisplaySubGenre)
 
def DeleteSubGenre(request, subId):
    subgen =SubGenreDb.objects.filter(id=subId)
    subgen.delete()
    messages.success(request, 'Deleted Successfully')
    return redirect(DisplaySubGenre)

################################# AUDIO #######################################################################

def AddAudio(request):
    lang = LanguageDb.objects.all()
    genre = GenreDb.objects.all()
    subgenre = SubGenreDb.objects.all()
    context = {'lang': lang, 'genre': genre, 'subgenre': subgenre}
    return render(request, 'directory/audio/add_audio.html', context)

def SaveAudio(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lang = request.POST.get('lang')
        genre = request.POST.get('genre')
        type = request.POST.get('type')
        year = request.POST.get('year')
        art = request.POST.get('artist')
        film = request.POST.get('film')
        aud = request.FILES['audio']
        img = request.FILES['image']
        ext = request.POST.get('extra')
        if SongsDb.objects.filter(Name=name).exists():
            messages.error(request, 'Audio file already Exists')
            return redirect(AddAudio)
        else:
            obj = SongsDb(Name=name, Language=lang, Genre=genre, Type=type, Year=year, Artist=art, Film=film, 
                Audio=aud, Image=img, Extra=ext)
            obj.save()
            messages.success(request, 'Upload Successfull')
            return redirect(AddAudio)

def DisplayAudio(request):
    audio = SongsDb.objects.all()
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            audio = SongsDb.objects.filter(Name__icontains=str)
    context = {'audio': audio}
    return render(request, 'directory/audio/disp_audio.html', context)

def EditAudio(request, audioId):
    lang = LanguageDb.objects.all()
    genre = GenreDb.objects.all()
    subgenre = SubGenreDb.objects.all()
    audio = SongsDb.objects.get(id=audioId)
    context = {'lang': lang, 'genre': genre, 'audio': audio, 'subgenre': subgenre}
    return render(request, 'directory/audio/edit_audio.html', context)

def UpdateAudio(request, audioId):
    if request.method == "POST":
        name = request.POST.get('name')
        lang = request.POST.get('lang')
        genre = request.POST.get('genre')
        type = request.POST.get('type')
        year = request.POST.get('year')
        art = request.POST.get('artist')
        film = request.POST.get('film')
        ext = request.POST.get('extra')
        try:
            aud = request.FILES['audio']
            file1 = FileSystemStorage().save(aud.name, aud)
            img = request.FILES['image']
            file2 = FileSystemStorage().save(img.name, img)
        except MultiValueDictKeyError:
            file1 = SongsDb.objects.get(id=audioId).Audio
            file2 = SongsDb.objects.get(id=audioId).Image
        if SongsDb.objects.filter(Name=name, Language=lang, Genre=genre, Type=type, Year=year,
                Artist=art, Film=film, Audio=file1, Image=file2, Extra=ext).exists():
            messages.warning(request, 'Data already Exists')
            return redirect(DisplayAudio)
        else:
            SongsDb.objects.filter(id=audioId).update(Name=name, Language=lang, Genre=genre, Type=type, Year=year,
                Artist=art, Film=film, Audio=file1, Image=file2, Extra=ext)
            messages.success(request, 'Updation Successfull')
            return redirect(DisplayAudio)      

def DeleteAudio(request, audioId):
    audio = SongsDb.objects.filter(id=audioId)
    audio.delete()
    messages.success(request, 'Deletion Successfull')
    return redirect(DisplayAudio)

############################### USERS ################################################################

def ViewUser(request):
    user = UsersDb.objects.all()
    context = {'user': user}
    return render(request, 'directory/users/view_user.html', context)

def RemoveUser(request, userId):
    user = UsersDb.objects.filter(id=userId)
    user.delete()
    messages.success(request, 'User Removal Successfull')
    return redirect(ViewUser)
