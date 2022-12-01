from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from MainApp import views

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'contacts',views.ContactView,'contact')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/",include('MainApp.urls')),
    path("",include('MainApp.urls')),
    path("about/",include('MainApp.urls')),
    path("accounts/",include('accounts.urls')),
    path("services/",include('MainApp.urls')),
    path("term/",include('MainApp.urls')),
    path("music/",include('Music.urls')),
    path("api/", include(router.urls)),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
