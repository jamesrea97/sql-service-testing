# sql-service-testing Project

# Testing

## Unit Testing

To ensure that atomic behaviour sufficiently coincided with the desired specifications, we generated unit tests using the `unittest` library.
A combination of `@patch` and `unittest.mock.MagicMock` were used in order to isolate various class behaviours so to ensure the testing was as singular as possible.

## Integration Testing

In order to gain a better overview of the process of extracting, transfering and inserting data from .csv to PostgreSQL, integration tests using Docker have been created. Through this container that contains data pre-loaded, we can have a better insight in overall process.

To carry out the integration test, please:

1. `cd` into project directory `~/test/integration_test/set_up`
2. Run Docker Container using `docker run -d --rm --name test-postgres-container --net=host -e POSTGRES_USER='test-user' -e POSTGRES_DB='test-tb' -e POSTGRES_PASSWORD='test' --mount source=./,destination=/opt postgres`
3. Execute initial data importing Docker commands `docker exec test-postgres-container psql -U test-user -d test-tb -f ./opt/setup/setup.sql`

Note: Although these steps could have been added to the Dockerfile, running on localhost caused initial issues. (Please comment if you belive this could be improved.)
