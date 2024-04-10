from django.urls import path
from frontend import views

urlpatterns = [
    path('Home/', views.frontindex, name='frontindex'),
    path('Profile/<user_flt>/', views.frontabout, name='frontabout'),
    #---------------------------------------------------------------------------------------------------------#
    path('Genre/<gnr_flt>/', views.GenreFiltered, name='GenreFiltered'),
    path('Type/<sub_flt>/', views.SubGenreFiltered, name='SubGenreFiltered'),
    path('Songs-List/<aud_flt>/', views.AudioListFiltered, name='AudioListFiltered'),
    path('Media-Player/<song_flt>/', views.SongFiltered, name='SongFiltered'),
    
    path('Add-Liked/', views.AddtoPlaylist, name='AddtoPlaylist'),
    path('Liked-Songs/<user_flt>/', views.ShowPlaylist, name='ShowPlaylist'),
    path('Delete-Likes/<song_flt>/', views.DeletePlaylist, name='DeletePlaylist'),
    path('Filter-Songs/<aud_flt>/', views.LikedSongFilter, name='LikedSongFilter'),
    path('Redirect/', views.FinalRedirect, name='FinalRedirect'),

    path('Form-Input/<user_flt>/', views.PlaylistForm, name='PlaylistForm'),
    path('Create-Playlist/', views.CreatePlaylist, name='CreatePlaylist'),
    path('Delete-Playlist/<lst_flt>/', views.DeleteCreatedPlaylist, name='DeleteCreatedPlaylist'),
    path('Add-Playlist/', views.AddtheSongs, name='AddtheSongs'),
    path('My-Playlist/<lst_flt>/', views.ViewtheSongs, name='ViewtheSongs'),
    path('Playlist/<aud_flt>/', views.PlaytheSong, name='PlaytheSong'),
    path('Delete-Songs/<lst_flt>/', views.DeletetheSongs, name='DeletetheSongs'),

    # LOGIN-PAGE 
    path('Login/', views.LoginPage, name='LoginPage'),
    path('Login-User/', views.LoginUser, name='LoginUser'),
    path('Logout-User/', views.LogoutUser, name='LogoutUser'),
    path('Signup/', views.SignupPage, name='SignupPage'),
    path('Save-User/', views.SaveUser, name='SaveUser'),
    path('Update-User/<user_flt>/', views.UpdateUser, name='UpdateUser'),

]
