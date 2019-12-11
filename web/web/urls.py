"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from music.views import hello_world,index,signup,post_signup,post_login,login,logout,GetArticleAPI
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('post_signup/',post_signup),    
    path('signup/',signup),
    path('post_login/',post_login),
    path('login/',login),
    path('logout/',logout),
    path('api/article',GetArticleAPI)

] + staticfiles_urlpatterns() 
# static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
# static(settings.IMAGES_URL , document_root=settings.IMAGES_ROOT)
