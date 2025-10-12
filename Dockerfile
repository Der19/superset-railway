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

# Start Superset (l'admin sera créé au premier démarrage)
CMD ["superset", "run", "-h", "0.0.0.0", "-p", "8088"]
