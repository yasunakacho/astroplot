"""astroplot URL Configuration

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
from django.conf.urls import url, include
from django.urls import include, path
from django.contrib.auth import urls, logout
from web import views
#from web.views import home, logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^detail/(?P<id>.+)/$', views.detail, name='detail'),
    url(r'^alert/(?P<id>.+)/$', views.alert, name='alert'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^logout/', views.logout, name='logout'),
#    url(r'^auth/', include('django.contrib.auth.views.logout', namespace='auth')),
#    url(r'^$', home, name='home'),
]
