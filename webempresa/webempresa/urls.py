"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
#cargamos el fichero settings de la carpeta webpersonal dentro de la memoria, ya que ahi sacaremos MEDIA_URL y MEDIA_ROOT
from django.conf import settings

urlpatterns = [
    #Path de la app blog
    path('blog/', include('blog.urls')),
	#path de la app core
	path('', include('core.urls')),
    #Path de la app services
    path('services/', include('services.urls')),
	#path de admin
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
