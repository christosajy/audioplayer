from django.urls import path
from frontend import views

urlpatterns = [
    path('HomePage/', views.frontindex, name='frontindex'),
    path('About-Us/', views.frontabout, name='frontabout'),
    path('Contact-Us/', views.frontcontact, name='frontcontact'),
    path('Combinations-Filtered/<cmb_flt>/', views.CombinationFiltered, name='CombinationFiltered'),
    path('player/', views.player, name='player'),
]
