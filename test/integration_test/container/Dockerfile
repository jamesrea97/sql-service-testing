FROM postgres:latest

# Exposing port
EXPOSE 5432

# Environment Variables for PostgreSQL connection
ENV POSTGRES_DB=test-db
ENV POSTGRES_USER=test-user
ENV POSTGRES_PASSWORD=test

# Copying data and setup folders

COPY . /opt

# Setting necessary permission 
RUN chmod +x /opt/setup/setup-script.sh
