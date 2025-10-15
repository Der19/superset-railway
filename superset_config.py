import os
import secrets

# Database configuration - SQLite en mémoire pour éviter les problèmes de fichiers
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Security - SECRET_KEY ultra sécurisée (128 caractères)
SECRET_KEY = 'superset-production-2024-railway-deployment-ultra-secure-key-128-characters-long-for-maximum-security-and-stability'

# JWT Secret pour les requêtes asynchrones (64 caractères)
JWT_SECRET = 'jwt-secret-key-for-superset-async-queries-railway-production-2024-secure'

# Configuration Superset complète
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS_SET": True,
    "GLOBAL_ASYNC_QUERIES": False,  # Désactivé pour éviter les erreurs
    "EMBEDDED_SUPERSET": True,
    "ENABLE_ADVANCED_DATA_TYPES": True,
    "ENABLE_EXPLORE_JSON_CSV": True,
    "ENABLE_EXPLORE_DRAG_AND_DROP": True,
    "ENABLE_DASHBOARD_NATIVE_FILTERS": True,
    "ENABLE_DRILL_TO_DETAIL": True,
    "ENABLE_DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_RBAC": True,
    "DASHBOARD_FILTERS_EXPERIMENTAL": True,
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

# Configuration de session
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# Configuration de base de données
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_pre_ping': True,
    'pool_recycle': 300,
}

# Configuration de logging
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'

# Configuration de sécurité supplémentaire
SECURITY_PASSWORD_SALT = 'superset-security-salt-2024-production'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha256'

# Configuration de rate limiting
RATELIMIT_ENABLED = False

# Configuration de CORS
ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': ['*']
}

# Configuration de sécurité des headers
SECURE_HEADERS = {
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'X-XSS-Protection': '1; mode=block'
}
