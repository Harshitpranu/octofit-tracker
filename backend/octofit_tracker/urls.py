from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework.urls import urlpatterns as drf_urlpatterns
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'api': request.build_absolute_uri(''),
    })

from django.views.generic import RedirectView

urlpatterns = [
	path('', RedirectView.as_view(url='/api/', permanent=False)),
	path('api/', api_root, name='api-root'),
	# All API endpoints should be included under /api/ here
]
