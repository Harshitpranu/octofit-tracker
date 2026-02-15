from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from django.views.generic import RedirectView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

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

@api_view(["GET"])
def codespaces_api_root(request, format=None):
    CODESPACE_NAME = os.environ.get("CODESPACE_NAME")
    if CODESPACE_NAME:
        base = f"https://{CODESPACE_NAME}-8000.app.github.dev/api/"
    else:
        # fallback for local dev, but lab expects Codespaces URL only
        base = "/api/"
    return Response({
        "users": base + "users/",
        "teams": base + "teams/",
        "activities": base + "activities/",
        "workouts": base + "workouts/",
        "leaderboard": base + "leaderboard/",
    })

urlpatterns = [
    path("", RedirectView.as_view(url="/api/", permanent=False)),
    path("api/", codespaces_api_root, name="api-root"),
    path("api/", include(router.urls)),
]

