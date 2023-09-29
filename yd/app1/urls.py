from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path("", views.youtube, name="home"), 
    path("get_resolution/", views.get_resolution, name="options"),
    path("download/", views.download, name="download"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)