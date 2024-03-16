from django.urls import path
from backend import views

urlpatterns = [
    path('backindex/', views.backindex, name='backindex'),
    path('addlang/', views.addlang, name='addlang'),
    path('savelang/', views.savelang, name='savelang'),
    path('displaylang/', views.displaylang, name='displaylang'),
    path('deletelang/<int:langId>/', views.deletelang, name='deletelang'),

    path('add_genre/', views.add_genre, name='add_genre'),
    path('save_genre/', views.save_genre, name='save_genre'),
    path('disp_genre/', views.disp_genre, name='disp_genre'),
    path('delete_genre/<int:genreId>/', views.delete_genre, name='delete_genre'),


    path('addaudio/', views.addaudio, name='addaudio'),
    path('saveaudio/', views.saveaudio, name='saveaudio'),
    path('displayaudio/', views.displayaudio, name='displayaudio'),
    path('editaudio/<int:audioId>/', views.editaudio, name='editaudio'),
    path('audiodelete/<int:audioId>/', views.audiodelete, name='audiodelete'),
]
