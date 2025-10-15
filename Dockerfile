FROM apache/superset:latest

# Install dependencies
USER root
RUN pip install --no-cache-dir \
    flask-cors \
    flask-openid \
    psycopg2-binary \
    flask-appbuilder \
    flask-babel \
    flask-migrate \
    flask-sqlalchemy \
    flask-wtf \
    wtforms \
    sqlalchemy \
    alembic

# Switch back to superset user
USER superset

# Copy configuration
COPY superset_config.py /app/pythonpath/superset_config.py

# Expose port
EXPOSE 8088

# Start Superset SANS authentification
CMD ["sh", "-c", "superset db upgrade && superset run -h 0.0.0.0 -p 8088"]
