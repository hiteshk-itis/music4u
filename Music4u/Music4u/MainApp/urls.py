from django.urls import path 
from . import views

urlpatterns = [
    path("",views.main_page),
    path("contact/",views.contact),
    path("about/",views.about),
    path("contact/",views.contact),
    path("services/",views.services),
    path("term/",views.term)
]