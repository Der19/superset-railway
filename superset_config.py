import os

# Database configuration - utiliser SQLite en mémoire pour éviter les problèmes de fichiers
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Security
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-change-this-in-production')

# Feature flags
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS_SET": True,
    "GLOBAL_ASYNC_QUERIES": True,
    "EMBEDDED_SUPERSET": True,
}

# CORS configuration for public access
WTF_CSRF_ENABLED = False
WTF_CSRF_TIME_LIMIT = None

# Public access configuration
PUBLIC_ROLE_LIKE_GAMMA = True

# Cache configuration
CACHE_CONFIG = {
    'CACHE_TYPE': 'simple',
}

# Logging
LOG_LEVEL = 'INFO'
