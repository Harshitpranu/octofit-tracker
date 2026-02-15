from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
 # Register your viewsets here if needed, e.g.:
 # router.register(r'users', UserViewSet)

from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=False)),
    path('api/', include(router.urls)),
]
