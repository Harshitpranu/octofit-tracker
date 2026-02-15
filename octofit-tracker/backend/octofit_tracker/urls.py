from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from django.views.generic import RedirectView

from .views import (
    UserViewSet,
    TeamViewSet,
    ActivityViewSet,
    LeaderboardViewSet,
    WorkoutViewSet,
)

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"teams", TeamViewSet, basename="team")
router.register(r"activities", ActivityViewSet, basename="activity")
router.register(r"workouts", WorkoutViewSet, basename="workout")
router.register(r"leaderboard", LeaderboardViewSet, basename="leaderboard")

urlpatterns = [
    path("", RedirectView.as_view(url="/api/", permanent=False)),
    path("api/", include(router.urls)),
]

