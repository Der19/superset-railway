FROM apache/superset:latest

# Install ALL missing dependencies
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

# Start Superset with CORRECT admin creation (sans duplication)
CMD ["sh", "-c", "superset db upgrade && superset fab create-admin --username admin --firstname Admin --lastname User --email admin@example.com --password admin && superset init && superset run -h 0.0.0.0 -p 8088"]
