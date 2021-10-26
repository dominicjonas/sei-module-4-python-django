from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from piece.views import PieceViewSet

router = routers.DefaultRouter()
router.register("pieces", PieceViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('composers/', include('composers.urls')),
   
]
