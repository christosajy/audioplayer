from django.urls import path
from frontend import views

urlpatterns = [
    path('Home/', views.frontindex, name='frontindex'),
    path('My_Profile/<user_flt>/', views.frontabout, name='frontabout'),
    #---------------------------------------------------------------------------------------------------------#
    path('Genre_Filtered/<gnr_flt>/', views.GenreFiltered, name='GenreFiltered'),
    path('Sub_Genre_Filtered/<sub_flt>/', views.SubGenreFiltered, name='SubGenreFiltered'),
    path('Sub_Genre_Songs_Filtered/<aud_flt>/', views.AudioListFiltered, name='AudioListFiltered'),
    path('Single_Songs_Filtered/<song_flt>/', views.SongFiltered, name='SongFiltered'),
    path('Add_To_Playlist/', views.AddtoPlaylist, name='AddtoPlaylist'),
    path('Show_Playlist/<user_flt>/', views.ShowPlaylist, name='ShowPlaylist'),
    path('Delete_Playlist/<song_flt>/', views.DeletePlaylist, name='DeletePlaylist'),
    path('LikedSongFilter/<aud_flt>/', views.LikedSongFilter, name='LikedSongFilter'),
    path('Redirect/', views.FinalRedirect, name='FinalRedirect'),

    # LOGIN-PAGE 
    path('Login_Page/', views.LoginPage, name='LoginPage'),
    path('Login_User/', views.LoginUser, name='LoginUser'),
    path('Logout_User/', views.LogoutUser, name='LogoutUser'),
    path('Signup_Page/', views.SignupPage, name='SignupPage'),
    path('Save_User/', views.SaveUser, name='SaveUser'),
    path('Update_User/<user_flt>/', views.UpdateUser, name='UpdateUser'),

]
