FROM bitnami/spark:3.3.0

# Create directory for custom scripts
RUN mkdir -p /opt/bitnami/spark/custom-scripts

# Copy your application code
COPY src/real_time_pipeline.py /opt/bitnami/spark/custom-scripts/

# Install necessary Spark dependencies
RUN /opt/bitnami/spark/bin/spark-shell --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 -i /dev/null

# Entrypoint to ensure the package is available on startup
ENTRYPOINT ["/opt/bitnami/spark/bin/spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0", "/opt/bitnami/spark/custom-scripts/real_time_pipeline.py"]
