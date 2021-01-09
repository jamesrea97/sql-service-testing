## Integration Testing

In order to gain a better overview of the process of extracting, transfering and inserting data from .csv to PostgreSQL, integration tests using Docker have been created. Through this container that contains data pre-loaded, we can have a better insight in overall process.

To carry out the integration test, please:

1. `cd` into project directory `~/test/integration_test/container`
2. Build Docker Image using `docker build . -t test-postgres-image`
3. Run Docker Container using `docker run -d --rm -p 5432:5432 --name test-postgres-container test-postgres-image`
4. Execute initial data importing Docker commands `docker exec -it test-postgres-container /opt/setup/setup-script.sh`
   `

Note: It is important to ensure that no other PostgreSQL service is currently using the port 5432 on your local machine as this will block the container from using the port.
