from django.urls import path
from frontend import views

urlpatterns = [
    path('HomePage/', views.frontindex, name='frontindex'),
    path('My-Profile/', views.frontabout, name='frontabout'),
    path('Genre-Filtered/<cmb_flt>/', views.GenreFiltered, name='GenreFiltered'),
    path('Sub-Genre-Filtered/<sub_flt>/', views.SubGenreFiltered, name='SubGenreFiltered'),
    path('Sub-Genre-Songs-Filtered/<aud_flt>/', views.AudioListFiltered, name='AudioListFiltered'),
    path('Single-Songs-Filtered/<song_flt>/', views.SongFiltered, name='SongFiltered'),
    # Login-Page 
    path('Login-Page/', views.LoginPage, name='LoginPage'),
]
