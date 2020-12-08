"""adminpanel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path ,include
from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^index/',views.index,name="index"),
    url(r'^tables/',views.tables,name="tables"),
    url(r'^charts/',views.charts,name="charts"),
    url(r'^cards/',views.cards,name="cards"),
    url(r'^500/',views.e500,name="e500"),
    url(r'^404/',views.e404,name="e404"),
    url(r'^401/',views.e401,name="e401"),
    url(r'^login/',views.login,name="login"),
    url(r'^register/',views.register,name="register"),
    url(r'^light/',views.layout,name="layout"),
    url(r'^base/',views.base,name="base"),

    url(r'^logout/',views.logout,name="logout"),
    path('password_reset_form/',
    auth_views.PasswordResetView.as_view(),
    name='password_reset_form'),

    path('password_reset/done/',
    auth_views.PasswordResetDoneView.as_view(),
    name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(),
    name='password_reset_confirm'),

    path('reset/done/',
    auth_views.PasswordResetCompleteView.as_view(),
    name='password_reset_complete'),








]
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
