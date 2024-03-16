from django.urls import path
from backend import views

urlpatterns = [
    path('home/', views.backindex, name='backindex'),
    path('add-language/', views.addlang, name='addlang'),
    path('save-language/', views.savelang, name='savelang'),
    path('display-language/', views.displaylang, name='displaylang'),
    path('delete-language/<int:langId>/', views.deletelang, name='deletelang'),

    path('add-genre/', views.add_genre, name='add_genre'),
    path('save-genre/', views.save_genre, name='save_genre'),
    path('display-genre/', views.disp_genre, name='disp_genre'),
    path('edit-genre/<int:genreId>/', views.edit_genre, name='edit_genre'),
    path('update-genre/<int:genreId>/', views.update_genre, name='update_genre'),
    path('delete-genre/<int:genreId>/', views.delete_genre, name='delete_genre'),


    path('add-audio/', views.addaudio, name='addaudio'),
    path('save-audio/', views.saveaudio, name='saveaudio'),
    path('display-audio/', views.displayaudio, name='displayaudio'),
    path('edit-audio/<int:audioId>/', views.editaudio, name='editaudio'),
    path('update-audio/<int:audioId>/', views.updateaudio, name='updateaudio'),
    path('audio-delete/<int:audioId>/', views.audiodelete, name='audiodelete'),
]
