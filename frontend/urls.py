from django.urls import path
from frontend import views

urlpatterns = [
    path('frontindex/', views.frontindex, name='frontindex'),
    path('frontabout/', views.frontabout, name='frontabout'),
    path('frontcontact/', views.frontcontact, name='frontcontact'),
    path('audiolist/<sng_flt>/', views.audiolist, name='audiolist'),
    path('player/', views.player, name='player'),
]
