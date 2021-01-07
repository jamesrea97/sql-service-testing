## Integration Testing

In order to gain a better overview of the process of extracting, transfering and inserting data from .csv to PostgreSQL, integration tests using Docker have been created. Through this container that contains data pre-loaded, we can have a better insight in overall process.

To carry out the integration test, please:

1. `cd` into project directory `~/test/integration_test/container`
2. Run Docker Container using `docker run -d --rm --name test-postgres-container --net=host -v $(pwd):/opt postgres`
3. Execute initial data importing Docker commands `docker exec test-postgres-container psql -U test-user -d test-tb -f ./opt/setup/setup.sql`
