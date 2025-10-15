import os

# Database configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Security
SECRET_KEY = 'superset-simple-key-2024'

# Basic configuration
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS_SET": True,
    "GLOBAL_ASYNC_QUERIES": False,
    "EMBEDDED_SUPERSET": True,
}

# Security settings
WTF_CSRF_ENABLED = False
WTF_CSRF_TIME_LIMIT = None

# Access settings
PUBLIC_ROLE_LIKE_GAMMA = True

# Cache
CACHE_CONFIG = {
    'CACHE_TYPE': 'simple',
}

# Logging
LOG_LEVEL = 'INFO'
