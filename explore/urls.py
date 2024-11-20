
from django.urls import path
from . import views


urlpatterns = [
        path('',views.tweet_list, name='tweer_list'),
        path('tweet/',views.tweet, name='tweet'),    
        path('tweet_list/', views.tweet_list, name='tweet_list'),
        path('register/',views.register, name='register'),
        path('profile_view/<int:profile_id>', views.profile_view, name='profile_view'),
            ]