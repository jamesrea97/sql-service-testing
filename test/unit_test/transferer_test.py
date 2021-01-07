""" Module unit tests Transferer class behaviour """

import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

import context
import test_environment

import extractor as extractor
import transferer as transferer
import database as database


class ShouldTransferData(unittest.TestCase):

    def setUp(self):
        ''' Sets up the data_path and sql_query '''
        self.data_path = 'path/to/data'
        self.sql_query = 'sql-query'

    @patch('database.Database')
    def test_transfers_data_from_file_to_db(self, mock_db):
        ''' Passes test if data is transfered from file to db '''

        extractor.Extractor.extract = MagicMock(
            return_value=['foo', 'bar'])

        trans = transferer.Transferer(mock_db)
        trans.transfer(self.data_path, self.sql_query)

        mock_db.insert.assert_called_with(['foo', 'bar'], self.sql_query)


if __name__ == "__main__":
    unittest.main()
