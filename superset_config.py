import os

# Database configuration - SQLite en mémoire
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Security - SECRET_KEY sécurisée
SECRET_KEY = 'superset-production-2024-railway-deployment-ultra-secure-key-128-characters-long-for-maximum-security-and-stability'

# Configuration Superset de base
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS_SET": True,
    "GLOBAL_ASYNC_QUERIES": False,
    "EMBEDDED_SUPERSET": True,
}

# Configuration de sécurité
WTF_CSRF_ENABLED = False
WTF_CSRF_TIME_LIMIT = None

# Configuration d'accès
PUBLIC_ROLE_LIKE_GAMMA = True

# Cache configuration
CACHE_CONFIG = {
    'CACHE_TYPE': 'simple',
}

# Logging
LOG_LEVEL = 'INFO'
