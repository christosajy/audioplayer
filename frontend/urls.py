from django.urls import path
from frontend import views

urlpatterns = [
    path('HomePage/', views.frontindex, name='frontindex'),
    path('About-Us/', views.frontabout, name='frontabout'),
    path('Contact-Us/', views.frontcontact, name='frontcontact'),
    path('Genre-Filtered/<cmb_flt>/', views.CombinationFiltered, name='CombinationFiltered'),
    path('Sub-Genre-Filtered/<sub_flt>/', views.SubGenreFiltered, name='SubGenreFiltered'),
    path('Sub-Genre-Songs-Filtered/<aud_flt>/', views.AudioListFiltered, name='AudioListFiltered'),
    path('player/', views.player, name='player'),
]
