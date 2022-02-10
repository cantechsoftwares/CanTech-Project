from django.urls import path
from django.utils.translation import templatize
from cantech import views
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import authenticate, views as auth_views

from . import views

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('feedback-form',views.FeedbackForm.as_view(),name="feedback-form"),
    path('About-Us',views.AboutUs.as_view(),name="About-Us"),
    path('Coming-Soon',views.ComingSoon.as_view(),name="coming-soon"),
    path('Services',views.Services.as_view(),name="services"),
    path('Contact',views.Contact.as_view(),name="contact-us"),
    path('Developers',views.Developer.as_view(),name="developer"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)