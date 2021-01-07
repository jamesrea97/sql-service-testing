""" Module contains DatabaseHelper, a helper for testing behaviour against a DB """

import psycopg2
import os

class DatabaseHelper:

    @classmethod
    def _connect(cls):
        ''' Connects to PostgreSQL db '''
        conn = None
        try:
            conn = psycopg2.connect(host=os.environ['HOST'],
                                    database=os.environ['DATABASE'],
                                    user=os.environ['USER'],
                                    password=os.environ['PASSWORD'],
                                    port=os.environ['PORT'])
            conn.autocommit = True
        except:
            pass
        finally:
            return conn

    @classmethod
    def select(cls, query, fields=[]):
        ''' Selects data using query and fields if present'''
        data = []
        conn = cls._connect()
        if conn:
            try:
                cursor = conn.cursor()

                data = cursor.execute(query, field)
                if isinstance(data[0], list):
                    cursor.executemany(query, data)
                else:
                    cursor.execute(query, data)

            except:
                pass
            finally:
                cursor.close()
                conn.close()
        return data
