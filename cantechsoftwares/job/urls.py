from django.urls import path
from django.utils.translation import templatize
from job import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import authenticate, views as auth_views

from . import views

urlpatterns = [
    path('',views.Portal.as_view(),name="Portal"),
    path('admin-login',views.Admin_login.as_view(),name="admin-login"),
    path('user-login',views.User_login.as_view(),name="user-login"),
    path('recruiter-login',views.Recruiter_login.as_view(),name="recruiter-login"),
    path('Signup',views.Signup.as_view(),name="signup"),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)