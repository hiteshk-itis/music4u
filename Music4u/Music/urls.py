from django.urls import path 
from . import views

urlpatterns = [
    #path("getmusic/",views.Viewmusic),
    path("postmusic/",views.Postmusic),
]