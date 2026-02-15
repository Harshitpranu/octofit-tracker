from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': request.build_absolute_uri('users/'),
		'teams': request.build_absolute_uri('teams/'),
		'activities': request.build_absolute_uri('activities/'),
		'leaderboard': request.build_absolute_uri('leaderboard/'),
		'workouts': request.build_absolute_uri('workouts/'),
	})

urlpatterns = [
	path('api/', api_root, name='api-root'),
	# path('api/users/', ...),
	# path('api/teams/', ...),
	# path('api/activities/', ...),
	# path('api/leaderboard/', ...),
	# path('api/workouts/', ...),
]
