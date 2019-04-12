"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin

from .views import home, contact, signin, register, signout

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^contact/$', contact, name="contact"),
    url(r'^login/$', signin, name="signin"),
    url(r'^logout/$', signout, name="signout"),
    url(r'^register/$', register, name="register"),
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include("products.urls", namespace="products")),
    url(r'^search/', include("search.urls", namespace="search")),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
