from django.contrib import admin
from django.urls import path,include
from news import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('allnews/',AllNews.as_view()),

]
