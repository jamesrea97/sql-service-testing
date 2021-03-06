import psycopg2

import logging
import os


class Database:

    def __init__(self):
        ''' Initializes fields for db connection '''
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
            conn.autocommit = True
        except:
            logging.error('An error has occured in connecting to the db...')
            pass
        else:
            logging.info('Successful connection...')
        finally:
            return conn

    def insert(self, data, query):
        ''' Insert data to db '''
        if data:
            conn = self._connect()

            if conn:
                try:
                    cursor = conn.cursor()

                    logging.info('Executing query')

                    if isinstance(data[0], list):
                        cursor.executemany(query, data)
                    else:
                        cursor.execute(query, data)

                except:

                    logging.error(
                        'An error has occured in inserting the data in the db...')
                else:
                    print('Successful upload of data... ')
                    logging.info('Successful upload of data...')
                finally:
                    cursor.close()
                    conn.close()
