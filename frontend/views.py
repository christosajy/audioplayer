from django.shortcuts import render, redirect
from backend.models import LanguageDb, GenreDb, SubGenreDb, SongsDb
from frontend.models import UsersDb, LikedSongs, CreatedPlaylist, AddSongs
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse

########################### HOME #############################################################################

def frontindex(request):
    lang = LanguageDb.objects.all()
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            lang = LanguageDb.objects.filter(Lang_Name__icontains=str)
    context = {'lang': lang}
    return render(request, 'home.html', context)

def GenreFiltered(request, gnr_flt):
    genre = GenreDb.objects.filter(LangName=gnr_flt)
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            genre = GenreDb.objects.filter(LangName__icontains=str)
    context = {'genre': genre}
    return render(request, 'directory/gnr_fltr.html', context)
    
def SubGenreFiltered(request, sub_flt):
    subgenre = SubGenreDb.objects.filter(GenreName=sub_flt)
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            subgenre = SubGenreDb.objects.filter(GenreName__icontains=str)
    context = {'subgenre': subgenre}
    return render(request, 'directory/sbgnr_fltr.html', context)

def AudioListFiltered(request, aud_flt):
    audio = SongsDb.objects.filter(Type=aud_flt)
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            audio = SongsDb.objects.filter(Type__icontains=str)
    context = {'audio': audio}
    return render(request, 'directory/list_fltr.html', context)

def SongFiltered(request, song_flt):
    if 'Username' not in request.session:
        song = SongsDb.objects.filter(Name=song_flt)
        context = {'song': song}
        return render(request, 'directory/song_fltr.html', context)
    else:
        login_user = request.session['Username'] 
        song = SongsDb.objects.filter(Name=song_flt)
        my_list = CreatedPlaylist.objects.filter(UserName=login_user)
        context = {'song': song, 'my_list': my_list}
        return render(request, 'directory/song_fltr.html', context)
   
############ LIKED-SONGS ######################################################################################

def AddtoPlaylist(request):
    if request.method == 'POST':
        snm = request.POST.get('song')
        usr = request.POST.get('user')
        art = request.POST.get('artist')
        obj = LikedSongs(SongName=snm, UserName=usr, ArtistName=art)
        if LikedSongs.objects.filter(SongName=snm).exists():
            messages.warning(request, 'Song already Exists.')
            return redirect(SongFiltered, user_flt = usr)
        else:
            obj.save()
            messages.success(request, 'Song added Successfully.')
            return redirect(SongFiltered, user_flt = usr)

def ShowPlaylist(request, user_flt):
    playlist = LikedSongs.objects.filter(UserName=user_flt)
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            playlist = LikedSongs.objects.filter(SongName__icontains=str)
    context = {'playlist': playlist}
    return render(request, 'playlist/liked_songs.html', context)

def DeletePlaylist(request, song_flt):
    playlist = LikedSongs.objects.filter(SongName=song_flt)
    playlist.delete()
    messages.success(request, 'Song removed Successfully.')
    return redirect(frontindex)

def LikedSongFilter(request, aud_flt):
    song = SongsDb.objects.filter(Name=aud_flt)
    context = {'song': song}
    return render(request, 'directory/song_fltr.html', context)

def FinalRedirect(request):
    return render(request, 'main/redirect.html')

###################################### MY-PLAYLIST-PAGE #######################################################

def PlaylistForm(request, user_flt):
    user = CreatedPlaylist.objects.filter(UserName=user_flt)
    if request.method == 'GET':
        str = request.GET.get('keyword')
        if str != None:
            user = CreatedPlaylist.objects.filter(PlaylistName__icontains=str)
    context =  {'user': user}
    return render(request, 'playlist/add_to.html', context)

def CreatePlaylist(request):
    if request.method == 'POST':
        nam = request.POST.get('name')
        usr = request.POST.get('user')
        obj = CreatedPlaylist(PlaylistName=nam, UserName=usr)
        if CreatedPlaylist.objects.filter(PlaylistName=nam).exists():
            messages.error(request, 'Please re-enter playlist name with an extra charecter.')
            return redirect(PlaylistForm, user_flt=usr)
        else:
            obj.save()
            messages.success(request, 'Playlist creation Successful')
            return redirect(PlaylistForm, user_flt=usr)    
        
def DeleteCreatedPlaylist(request, lst_flt):
    playlist = CreatedPlaylist.objects.filter(PlaylistName=lst_flt)
    playlist.delete()
    messages.success(request, 'Playlist removal Successful')
    return redirect(FinalRedirect)


###################################### ADD-TO-PLAYLIST #######################################################

def AddtheSongs(request):
    if request.method == 'POST':
        nam = request.POST.get('name')
        pst = request.POST.get('playlist')
        usr = request.POST.get('user')
        obj = AddSongs(PlaylistName=pst, SongName=nam, UserName=usr)
        if AddSongs.objects.filter(SongName=nam, PlaylistName=pst).exists():
            messages.error(request, 'Song already Exists')
            return redirect(FinalRedirect)
        else:
            obj.save()
            messages.success(request, 'Song added to Playlist')
            return redirect(FinalRedirect)
        
def ViewtheSongs(request, lst_flt):
    playlist = AddSongs.objects.filter(PlaylistName=lst_flt)
    context =  {'playlist': playlist}
    return render(request, 'playlist/view_playlist.html', context)

def PlaytheSong(request, aud_flt):
    song = SongsDb.objects.filter(Name=aud_flt)
    context = {'song': song}
    return render(request, 'directory/song_fltr.html', context)

def DeletetheSongs(request, lst_flt):
    playlist = AddSongs.objects.filter(SongName=lst_flt)
    playlist.delete()
    messages.success(request, 'Song removed from Playlist')
    return redirect(frontindex)
 
###################################### PROFILE-PAGE #########################################################

def frontabout(request, user_flt):
    user = UsersDb.objects.filter(Username=user_flt).first()
    context = {'user': user}
    return render(request, 'main/my_profile.html', context)

def LoginPage(request):
    return render(request, 'forms/login.html')

def LoginUser(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        ps = request.POST.get('pass')
        if UsersDb.objects.filter(Username=un, Password=ps).exists():
            request.session['Username'] = un
            request.session['Password'] = ps
            messages.success(request, 'Login Successful. Welcome Home')
            return redirect(frontindex)
        else:
            messages.warning(request, 'User not found. Create new?')
            return redirect(SignupPage)

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
            return redirect(LoginPage)

def UpdateUser(request, user_flt):
    if request.method == 'POST':
        nm = request.POST.get('name')
        em = request.POST.get('email')
        un = request.POST.get('uname')
        ps = request.POST.get('pass')
        try:
            im = request.FILES['img']
            file = FileSystemStorage().save(im.name,im)
        except MultiValueDictKeyError:
            file = UsersDb.objects.get(Username=user_flt).Profile
        UsersDb.objects.filter(Username=user_flt).update(Name=nm, Email=em, Username=un, Password=ps, Profile=file)
        del request.session['Username']
        del request.session['Password']
        messages.success(request, 'Data Updated Successfully. User Logged off. Re-Login again.')
        return redirect(frontindex)
