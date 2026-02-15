
import os
from django.urls import path, include
from django.views.generic import RedirectView

# Codespaces: expose API at /api/ and root redirect
CODESPACE_NAME = os.environ.get("CODESPACE_NAME")
codespace_url = f"https://{CODESPACE_NAME}-8000.app.github.dev" if CODESPACE_NAME else None

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=False)),
    path('api/', include('octofit_tracker.urls')),
]

