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
    path('Delete_Genre/<int:genreId>/', views.DeleteGenre, name='DeleteGenre'),

    path('Add_Sub_Genre/', views.AddSubGenre, name='AddSubGenre'),
    path('Save_Sub_Genre/', views.SaveSubGenre, name='SaveSubGenre'),
    path('Display_Sub_Genre/', views.DisplaySubGenre, name='DisplaySubGenre'),
    path('Edit_Sub_Genre/<int:subId>/', views.EditSubGenre, name='EditSubGenre'),
    path('Update_Sub_Genre/<int:subId>/', views.UpdateSubGenre, name='UpdateSubGenre'),
    path('Delete_Sub_Genre/<int:subId>/', views.DeleteSubGenre, name='DeleteSubGenre'),

    path('Add_Genre_Combination/', views.AddCombination, name='AddCombination'),
    path('Edit_Genre_Combination/<int:combId>', views.EditCombination, name='EditCombination'),
    path('Update_Genre_Combination/<int:combId>/', views.UpdateCombination, name='UpdateCombination'),
    path('Save_Genre_Combination/', views.SaveCombination, name='SaveCombination'),
    path('Display_Genre_Combination/', views.DisplayCombination, name='DisplayCombination'),
    path('Display_Genre_Combination/<int:combId>/', views.DeleteCombination, name='DeleteCombination'),

    path('Add_Subgenre_Combination', views.AddSubCombination, name='AddSubCombination'),
    path('Save_Subgenre_Combination', views.SaveSubCombination, name='SaveSubCombination'),
    path('Display_Subgenre_Combination', views.DisplaySubCombination, name='DisplaySubCombination'),
    path('Edit_Subgenre_Combination/<int:subId>', views.EditSubCombination, name='EditSubCombination'),
    path('Update_Subgenre_Combination/<int:subId>', views.UpdateSubCombination, name='UpdateSubCombination'),
    path('Delete_Subgenre_Combination/<int:subId>/', views.DeleteSubCombination, name='DeleteSubCombination'),

    path('Add_Audio/', views.AddAudio, name='AddAudio'),
    path('Save_Audio/', views.SaveAudio, name='SaveAudio'),
    path('Display_Audio/', views.DisplayAudio, name='DisplayAudio'),
    path('Edit_Audio/<int:audioId>/', views.EditAudio, name='EditAudio'),
    path('Update_Audio/<int:audioId>/', views.UpdateAudio, name='UpdateAudio'),
    path('Delete_Audio/<int:audioId>/', views.DeleteAudio, name='DeleteAudio'),

    path('View_User/', views.ViewUser, name='ViewUser'),
    path('Remove_User/<int:userId>/', views.RemoveUser, name='RemoveUser'),
]
