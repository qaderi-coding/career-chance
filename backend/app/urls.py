
from django.urls import path, include
from .router import router

urlpatterns = [

    path('app/', include(router.urls))
]