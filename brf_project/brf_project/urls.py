from django.contrib import admin
from django.urls import path,include
from brfapp.views import home
from rest_framework.routers import DefaultRouter
from brfapp.views import MumbaiRouteViewSet

router=DefaultRouter()
router.register(r'mumbai-routes',MumbaiRouteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path('api/',include(router.urls)),
]