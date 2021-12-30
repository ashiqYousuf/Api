from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path , include
from api import views


router = DefaultRouter()
router.register('studentapi',views.StudentAPI,basename='studentapi')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
