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

    # root endpoint
    path('', ecard_views.welcome),

    # admin endpoint
    path('admin/', admin.site.urls),

    # authentication endpoints
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),

    # user endpoints
    path('users/', ecard_views.UserList.as_view(), name='user-list'),
    path('users/follow/', ecard_views.FollowUser.as_view(),
         name='follow-user'),
    path('users/unfollow/<int:pk>', ecard_views.UnfollowUser.as_view(),
         name='unfollow-user'),
    path('following/', ecard_views.FollowingList.as_view(),
         name='following_list'),
    path('followers/', ecard_views.FollowerList.as_view(),
         name='followers_list'),

    # card endpoints
    path('cards/new/', ecard_views.NewCard.as_view(), name='new-card'),
    path('cards/<int:pk>/', ecard_views.CardDetail.as_view(),
         name='card-detail'),
    path('cards/', ecard_views.CardList.as_view(), name='card-list'),
    path('cards/timeline/', ecard_views.CardTimeline.as_view(),
         name='card-timeline'),
    path('profile/', ecard_views.Profile.as_view(), name='profile'),
]
