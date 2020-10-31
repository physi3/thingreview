from django.urls import path

from . import views


app_name = 'things'
urlpatterns = [
    path('', views.index, name='index'),
    path('thing/<int:id>/', views.thing, name='thing'),
    path('thing/<int:id>/review/', views.review, name='review'),
    path('things/', views.things, name='things'),
    path('things/thing/', views.make_thing, name='make_thing'),
    path('search/', views.search, name='search'),
    path('random/', views.random, name='random'),
    path('latest/', views.latest, name='latest'),
    path('least_reviewed/', views.least_reviewed, name='least_reviewed'),
]
