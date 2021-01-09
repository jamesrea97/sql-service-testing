# PostgreSQL Testing Sample Project

A simple unit/integratin tested PostgreSQL db script using Docker, Python's `mock` library.

## Aims of this project

This project is purposed for self-learning, specifically in writting testable code with a PostgreSQL Database.

Through this project, I have developped understanding of the Python development -> testing -> deployment pipeline.

More specifically, I have gained deeper understanding of:

- Python's `psycopg2` API for communicating with PostgreSQL Databases.
- Unit testing using `@patch` and `MagicMock`
- Integration testing using Docker, ensuring the actual database is not altered during testing
- Creating of deployment environment using `.env` and `environment.yml` files.

## Deployment

We assume that both `conda` package manager as well as `python=3.8` are installed on your machine.

In order to set up the dependencies environment, please run `./deployment.sh`, which will create the `conda` environment `sql-service-env` in your current directory, as well as install the relevant dependencies.

Activate your environment by running `conda activate sql-service-env`

From here, please run with command line arguments `python3 ./src/app.py SQL_QUERY_PATH DATA_QUERY_PATH `.

Note that an additional `.env` file inside the root directory containing your PostgreSQL listed below is required for the connection:

- `DATABASE=`
- `USER=`
- `PASSWORD=`
- `HOST=`
- `PORT=`

Note: this has only been tested on Ubuntu 20.04.

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

Note: It is important to ensure that no other PostgreSQL service is currently using the port 5432 on your local machine as this will block the container from using the port. This can be achieved on Linux as follows:

1. sudo kill -9 `sudo lsof -t -i:5432`

Beware that this will kill the current postgreSQL connection.

Once you are done with the container, remeber to stop the container by running `docker stop test-postgres-container`, which will automatically remove the container from your list of containers.

## Future work

Potential future work in adding more PostgreSQL commands, including selecting data, creating a DB, etc. could be implemented.
