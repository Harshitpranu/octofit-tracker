from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-key'
DEBUG = True

CODESPACE_NAME = os.environ.get("CODESPACE_NAME")

ALLOWED_HOSTS = [
    # Codespaces: allow the public URL for this codespace
    "localhost",
    "127.0.0.1",
    "[::1]",
]
if CODESPACE_NAME:
    ALLOWED_HOSTS.append(f"{CODESPACE_NAME}-8000.app.github.dev")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'octofit_tracker',
]
