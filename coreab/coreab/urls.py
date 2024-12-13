"""
URL configuration for coreab project.

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
from django.conf.urls.static import static
from appab.views import *
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='service'),
    path('test/', test, name='test'),
    path('register/', reg, name='register'),
    path('profil', profil, name='profil'),
    path('logout/', logout_view, name='logout'),
    path('vhod/', LoginUser.as_view(), name='vhod'),
    path('service-appointment/', service_appointment, name='service_appointment'),
    path('success/', lambda request: render(request, 'appab/success.html'), name='success'),
    path('eco/', eco, name='eco'),
    path('qr/', qr, name='qr'),
    path('userzapis/', userzapis, name='userzapis'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)