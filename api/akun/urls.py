from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from.views import *

router = DefaultRouter()
router.register('register', RegisterViewSet, basename='register')
router.register('login', LoginViewset, basename='login')
router.register('amil', RegisterAmilViewSet, basename='amil')
router.register('distribusi', DistribusiViewset, basename='distribusi')
router.register('zakat', ZakatViewset, basename='zakat')
urlpatterns = router.urls