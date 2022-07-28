"""quokka_cards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from ecards import views as ecard_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    path("api/auth/", include("djoser.urls.authtoken")),
    path('users/', ecard_views.UserList.as_view(), name='user-list'),
    path('cards/', ecard_views.cardlist.as_view(), name='card-list'),
    path('cards/new/', ecard_views.new_card.as_view(), name='new-card'),
    path('cards/<int:pk>/', ecard_views.carddetail.as_view(), name='card-detail'),
]
