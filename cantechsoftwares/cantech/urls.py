from django.urls import path
from django.utils.translation import templatize
from cantech import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import authenticate, views as auth_views

from . import views

urlpatterns = [
    path('',views.Home.as_view(),name="home"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)