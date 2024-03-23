from django.shortcuts import render, redirect
from backend.models import LanguageDb, CombinedDb, SubCombinedDb, SongsDb
from frontend.models import UsersDb
from django.contrib import messages

########################### HOME #############################################################################

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


###################################### PROFILE-PAGE ########################################################

def frontabout(request):
    return render(request, 'main/my_profile.html')

def LoginPage(request):
    return render(request, 'forms/login.html')

def LoginUser(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        ps = request.POST.get('pass')
        if UsersDb.objects.filter(Username=un, Password=ps).exists():
            # Setting Session
            request.session['Username'] = un
            request.session['Password'] = ps
            messages.success(request, 'Login Successful. Welcome Home')
            return redirect(frontindex)
        else:
            messages.warning(request, 'User not found. Create new?')
            return redirect(LoginPage)

def LogoutUser(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, 'User Logout Successfull')
    return redirect(frontindex)

def SignupPage(request):
    return render(request, 'forms/signup.html')

def SaveUser(request):
    if request.method == 'POST':
        nm = request.POST.get('name')
        em = request.POST.get('email')
        un = request.POST.get('uname')
        ps = request.POST.get('pass')
        if UsersDb.objects.filter(Email=em, Username=un).exists():
            messages.error(request, 'User already Exists')
            return redirect(SignupPage)
        else:
            obj = UsersDb(Name=nm, Email=em, Username=un, Password=ps)
            obj.save()
            messages.success(request, 'User Signup Successfull')
            return redirect(SignupPage)
