""" Module unit tests Database class behaviour """
import unittest
from unittest.mock import patch

import context
import test_environment

import os
import database as database


class ShouldInsertData(unittest.TestCase):

    def setUp(self):
        ''' Sets up data path '''
        self.db = database.Database()
        with open('src/sql/insert_users.sql') as query_file:
            self.query = query_file.read().replace('\n', '')

    @patch('psycopg2.connect')
    def test_can_insert_date_in_db(self, mock_connect):
        ''' Passes test if data correctly inserted '''

        self.db.insert(['James', 'Rea', 23, 'male', 'British'], self.query)

        mock_connect.return_value.cursor.assert_called()
        mock_connect.return_value.cursor.return_value.execute.assert_called()
        mock_connect.return_value.cursor.return_value.close.assert_called()
        mock_connect.return_value.close.assert_called()

    @patch('psycopg2.connect')
    def test_can_insert_no_data_in_db(self, mock_connect):
        ''' Passes test if data correctly inserted '''

        self.db.insert([], self.query)

        mock_connect.return_value.cursor.assert_not_called()

    @patch('psycopg2.connect')
    def test_can_insert_lots_of_data_in_db(self, mock_connect):
        ''' Passes test if data correctly inserted '''

        data = [['James', 'Rea', 23, 'male', 'British'],
                ['James', 'Rea', 23, 'male', 'British']]
        self.db.insert(data, self.query)

        mock_connect.return_value.cursor.assert_called()
        mock_connect.return_value.cursor.return_value.executemany.assert_called()
        mock_connect.return_value.cursor.return_value.close.assert_called()
        mock_connect.return_value.close.assert_called()


if __name__ == "__main__":
    unittest.main()
