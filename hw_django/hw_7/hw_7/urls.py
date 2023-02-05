from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from hw_permissions.views import AdvViewSet

r = DefaultRouter()
r.register('adv', AdvViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
] + r.urls
