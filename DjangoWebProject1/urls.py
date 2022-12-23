"""
Definition of urls for DjangoWebProject1.
"""

from django.contrib import admin
from django.conf.urls import include
admin.autodiscover()
import app.forms
import app.views 
from datetime import datetime
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('anketa/', views.anketa, name='anketa'),
    path('registration/', views.registration, name='registration'),
    path('blog/', views.blog, name='blog'),   
    path('(<int:parametr>\d+)/', views.blogpost, name='blogpost'),
    path('newpost/', views.newpost, name='newpost'),
    path('videopost/', views.videopost, name='videopost'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()