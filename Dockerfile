FROM apache/superset:latest

# Install additional dependencies
USER root
RUN pip install --no-cache-dir psycopg2-binary

# Switch back to superset user
USER superset

# Copy custom configuration and init script
COPY superset_config.py /app/pythonpath/superset_config.py
COPY init_admin.py /app/init_admin.py

# Expose port
EXPOSE 8088

# Start Superset with proper admin creation
CMD ["sh", "-c", "superset db upgrade && python /app/init_admin.py && superset init && superset run -h 0.0.0.0 -p 8088"]
