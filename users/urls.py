from django.urls import path
from .views import HelloView, RegisterApiView,LoginApiView,ProfileApiView

urlpatterns = [
        path('hello/', HelloView.as_view(), name='hello'),
        path('register', RegisterApiView.as_view(), name='register'),
        path('login',LoginApiView.as_view(),name='login'),
        path('profile',ProfileApiView.as_view(),name='profile'),
]