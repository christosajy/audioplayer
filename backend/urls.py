from django.urls import path
from backend import views

urlpatterns = [
    path('Home/', views.backindex, name='backindex'),
    path('Add_Language/', views.AddLanguage, name='AddLanguage'),
    path('Save_Language/', views.SaveLanguage, name='SaveLanguage'),
    path('Display_Language/', views.DisplayLanguage, name='DisplayLanguage'),
    path('Edit_Language/<int:langId>/', views.EditLanguage, name='EditLanguage'),
    path('Update_Language/<int:langId>/', views.UpdateLanguage, name='UpdateLanguage'),
    path('Delete_Language/<int:langId>/', views.DeleteLanguage, name='DeleteLanguage'),

    path('Add_Genre/', views.AddGenre, name='AddGenre'),
    path('Save_Genre/', views.SaveGenre, name='SaveGenre'),
    path('Display_Genre/', views.DisplayGenre, name='DisplayGenre'),
    path('Edit_Genre/<int:genreId>/', views.EditGenre, name='EditGenre'),
    path('Update_Genre/<int:genreId>/', views.UpdateGenre, name='UpdateGenre'),
    path('Delete_Genre/<int:genreId>/', views.DeleteGenre, name='DeleteGenre'),

    path('Add_Sub_Genre/', views.AddSubGenre, name='AddSubGenre'),
    path('Save_Sub_Genre/', views.SaveSubGenre, name='SaveSubGenre'),
    path('Display_Sub_Genre/', views.DisplaySubGenre, name='DisplaySubGenre'),
    path('Edit_Sub_Genre/<int:subId>/', views.EditSubGenre, name='EditSubGenre'),
    path('Update_Sub_Genre/<int:subId>/', views.UpdateSubGenre, name='UpdateSubGenre'),
    path('Delete_Sub_Genre/<int:subId>/', views.DeleteSubGenre, name='DeleteSubGenre'),

    path('Add_Audio/', views.AddAudio, name='AddAudio'),
    path('Save_Audio/', views.SaveAudio, name='SaveAudio'),
    path('Display_Audio/', views.DisplayAudio, name='DisplayAudio'),
    path('Edit_Audio/<int:audioId>/', views.EditAudio, name='EditAudio'),
    path('Update_Audio/<int:audioId>/', views.UpdateAudio, name='UpdateAudio'),
    path('Delete_Audio/<int:audioId>/', views.DeleteAudio, name='DeleteAudio'),

    path('View_User/', views.ViewUser, name='ViewUser'),
    path('Remove_User/<int:userId>/', views.RemoveUser, name='RemoveUser'),
]
