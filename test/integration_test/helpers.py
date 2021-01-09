""" Module contains Helpers for Integration testin """


import psycopg2
import os


class DatabaseHelper:
    ''' Helps connect to DB '''
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

                cursor.execute(query, fields)
                data = cursor.fetchall()
            except:
                pass
            finally:
                cursor.close()
                conn.close()
        return data


class QueryHelper:
    ''' Helps prepare query and compares results with PostgreSQL '''
    @classmethod
    def query_result_formatter(cls, data):
        ''' Formats data in a readable manner for test '''
        return [r[0].replace('(', '').replace(')', '').split(',') for r in data]

    @classmethod
    def query_builder(cls, path):
        ''' Builds query from file '''
        with open(path, 'r') as query_file:
            return query_file.read()

    @classmethod
    def query_comparor(cls, query_before, query_after):
        ''' Returns a list of elements present in query_after but not in query_before  '''
        result = []
        for entry in query_after:
            if entry not in query_before:
                result.append(entry)
        return result
