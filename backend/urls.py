from django.urls import path
from backend import views

urlpatterns = [
    path('HomePage/', views.backindex, name='backindex'),
    path('Add-Language-Genre/', views.AddLanguageAndGenre, name='AddLanguageAndGenre'),
    path('Save-Language/', views.SaveLanguage, name='SaveLanguage'),
    path('Display-Language/', views.DisplayLanguage, name='DisplayLanguage'),
    path('Delete-Language/<int:langId>/', views.DeleteLanguage, name='DeleteLanguage'),

    path('Save-Genre/', views.SaveGenre, name='SaveGenre'),
    path('Display-Genre/', views.DisplayGenre, name='DisplayGenre'),
    path('Edit-Genre/<int:genreId>/', views.EditGenre, name='EditGenre'),
    path('Update-Genre/<int:genreId>/', views.UpdateGenre, name='UpdateGenre'),
    path('Delete-Genre/<int:genreId>/', views.DeleteGenre, name='DeleteGenre'),

    path('Add-Genre-Language-Combination/', views.AddCombination, name='AddCombination'),
    path('Save-Genre-Language-Combination/', views.SaveCombination, name='SaveCombination'),
    path('Display-Genre-Language-Combination/', views.DisplayCombination, name='DisplayCombination'),
    path('Display-Genre-Language-Combination/<int:combId>/', views.DeleteCombination, name='DeleteCombination'),


    path('Add-Audio/', views.AddAudio, name='AddAudio'),
    path('Save-Audio/', views.SaveAudio, name='SaveAudio'),
    path('Display-Audio/', views.DisplayAudio, name='DisplayAudio'),
    path('Edit-Audio/<int:audioId>/', views.EditAudio, name='EditAudio'),
    path('Update-Audio/<int:audioId>/', views.UpdateAudio, name='UpdateAudio'),
    path('Delete-Audio/<int:audioId>/', views.DeleteAudio, name='DeleteAudio'),
]
