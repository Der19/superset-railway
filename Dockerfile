FROM apache/superset:latest

# Install additional dependencies
USER root
RUN pip install --no-cache-dir psycopg2-binary

# Switch back to superset user
USER superset

# Copy custom configuration
COPY superset_config.py /app/pythonpath/superset_config.py

# Expose port
EXPOSE 8088

# Start Superset avec initialisation
CMD ["sh", "-c", "superset db upgrade && superset fab create-admin --username admin --firstname Admin --lastname User --email admin@example.com --password admin && superset init && superset run -h 0.0.0.0 -p 8088"]
