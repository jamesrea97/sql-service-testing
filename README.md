# PostgreSQL Testing Sample Project

This project is purposed to create a simple testing environment for PostgreSQL database communication.A combination of Unit tests using Python's `unittest` testing library and Integration test using Docker containers are used.

# Deployment

TODO

# Testing

## Unit Testing

To ensure that atomic behaviour sufficiently coincided with the desired specifications, we generated unit tests using the `unittest` library.
A combination of `@patch` and `unittest.mock.MagicMock` were used in order to isolate various class behaviours so to ensure the testing was as singular as possible.

## Integration Testing

In order to gain a better overview of the process of extracting, transfering and inserting data from .csv to PostgreSQL, integration tests using Docker have been created. Through this container that contains data pre-loaded, we can have a better insight in overall process.

To carry out the integration test, please:

1. `cd` into project directory `~/test/integration_test/container`
2. Build Docker Image using `docker build . -t test-postgres-image`
3. Run Docker Container using `docker run -d --rm -p 5432:5432 --name test-postgres-container test-postgres-image`
4. Execute initial data importing Docker commands `docker exec -d test-postgres-container /opt/setup/setup-script.sh`

Once you have completed these 4 steps, you can start the integration tests found in `./test/integration_test/`
`

Note: It is important to ensure that no other PostgreSQL service is currently using the port 5432 on your local machine as this will block the container from using the port.

Remember to stop the container. This will automatically remove the container from your containers.
