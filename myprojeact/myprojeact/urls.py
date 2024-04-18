"""
URL configuration for myprojeact project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('', receipe_home, name='receipe_home'),
    path('receipe/', receipe, name='receipe'),
    path('view_page/<int:id>/', view_page, name='view_page'),
    path('view_receipe/', view_receipe, name='view_receipe'),
    path('edit_receipe/<int:id>/', edit_receipe, name='edit_receipe'),
    path('delete_receipe/<int:id>/', delete_receipe, name='delete_receipe'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout_user/', logout_user, name='logout_user'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)