
from django.urls import path, include
from .router import router

urlpatterns = [

    path('api/', include(router.urls))
]