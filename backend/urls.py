from django.urls import path
from backend import views

urlpatterns = [
    path('HomePage/', views.backindex, name='backindex'),
    path('Add-Language/', views.AddLanguage, name='AddLanguage'),
    path('Save-Language/', views.SaveLanguage, name='SaveLanguage'),
    path('Display-Language/', views.DisplayLanguage, name='DisplayLanguage'),
    path('Edit-Language/<int:langId>/', views.EditLanguage, name='EditLanguage'),
    path('Update-Language/<int:langId>/', views.UpdateLanguage, name='UpdateLanguage'),
    path('Delete-Language/<int:langId>/', views.DeleteLanguage, name='DeleteLanguage'),

    path('Add-Genre/', views.AddGenre, name='AddGenre'),
    path('Save-Genre/', views.SaveGenre, name='SaveGenre'),
    path('Display-Genre/', views.DisplayGenre, name='DisplayGenre'),
    path('Delete-Genre/<int:genreId>/', views.DeleteGenre, name='DeleteGenre'),

    path('Add-Sub-Genre/', views.AddSubGenre, name='AddSubGenre'),
    path('Save-Sub-Genre/', views.SaveSubGenre, name='SaveSubGenre'),
    path('Display-Sub-Genre/', views.DisplaySubGenre, name='DisplaySubGenre'),
    path('Edit-Sub-Genre/<int:subId>/', views.EditSubGenre, name='EditSubGenre'),
    path('Update-Sub-Genre/<int:subId>/', views.UpdateSubGenre, name='UpdateSubGenre'),
    path('Delete-Sub-Genre/<int:subId>/', views.DeleteSubGenre, name='DeleteSubGenre'),

    path('Add-Genre-Combination/', views.AddCombination, name='AddCombination'),
    path('Edit-Genre-Combination/<int:combId>', views.EditCombination, name='EditCombination'),
    path('Update-Genre-Combination/<int:combId>/', views.UpdateCombination, name='UpdateCombination'),
    path('Save-Genre-Combination/', views.SaveCombination, name='SaveCombination'),
    path('Display-Genre-Combination/', views.DisplayCombination, name='DisplayCombination'),
    path('Display-Genre-Combination/<int:combId>/', views.DeleteCombination, name='DeleteCombination'),

    path('Add-Subgenre-Combination', views.AddSubCombination, name='AddSubCombination'),
    path('Save-Subgenre-Combination', views.SaveSubCombination, name='SaveSubCombination'),
    path('Display-Subgenre-Combination', views.DisplaySubCombination, name='DisplaySubCombination'),
    path('Edit-Subgenre-Combination/<int:subId>', views.EditSubCombination, name='EditSubCombination'),
    path('Update-Subgenre-Combination/<int:subId>', views.UpdateSubCombination, name='UpdateSubCombination'),
    path('Delete-Subgenre-Combination/<int:subId>/', views.DeleteSubCombination, name='DeleteSubCombination'),

    path('Add-Audio/', views.AddAudio, name='AddAudio'),
    path('Save-Audio/', views.SaveAudio, name='SaveAudio'),
    path('Display-Audio/', views.DisplayAudio, name='DisplayAudio'),
    path('Edit-Audio/<int:audioId>/', views.EditAudio, name='EditAudio'),
    path('Update-Audio/<int:audioId>/', views.UpdateAudio, name='UpdateAudio'),
    path('Delete-Audio/<int:audioId>/', views.DeleteAudio, name='DeleteAudio'),
]
