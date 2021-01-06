import psycopg2

import logging
import os


class Database:

    def __init__(self):
        ''' Initializes fields for db connection '''
        # TODO make this an env file
        self._database = os.environ['DATABASE']
        self._user = os.environ['USER']
        self._password = os.environ['PASSWORD']
        self._host = os.environ['HOST']
        self._port = os.environ['PORT']

    def _connect(self):
        ''' Connects to PostgreSQL db '''
        conn = None
        try:
            logging.info(
                '''Connecting to PostGreSQL db: {} wirh hostname: {} 
                    and user: {} on port: {} ...'''.format(self._database,
                                                           self._host,
                                                           self._user,
                                                           self._port)
            )
            conn = psycopg2.connect(host=self._host,
                                    database=self._database,
                                    user=self._user,
                                    password=self._password,
                                    port=self._port)
        except:
            # TODO complete error handling
            logging.error('An error has occured')
            pass
        else:
            logging.info('Successful connection...')
        finally:
            return conn

    def insert(self, data, query):
        ''' Insert data to db '''
        conn = self._connect()

        if conn:
            try:
                cursor = conn.cursor()

                logging.info('Executing query')
                cursor.execute(data, query)

            except:
                # TODO complete error handling
                logging.error('An error has occured')
            else:
                logging.info('Successful upload of data...')
            finally:
                conn.commit()
                conn.close()


if __name__ == "__main__":
    d = Database()

    d._connect()
