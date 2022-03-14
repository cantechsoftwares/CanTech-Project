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
    path('Signup',views.Signup.as_view(),name="Signup"),
    path('Logout',views.Logout.as_view(),name="Logout"),
    path('Administrator',views.Administrator.as_view(),name="Administrator"), 
    path('delete_url/<int:pid>/<str:type>',views.delete_url.as_view(),name="delete_url"), 
    path('change_status/<int:pid>',views.change_status.as_view(),name="change_status"), 
    path('change_password',views.change_password.as_view(),name="change_password"), 
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)