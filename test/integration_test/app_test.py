""" Module integration tests App behaviour """

import unittest

from dotenv import load_dotenv
import context
import os

from app import run

from helpers.database_helper import DatabaseHelper
from helpers.query_helper import QueryHelper


class ShouldIntegrateData(unittest.TestCase):

    def setUp(self):
        ''' Sets up environment for integration test '''
        self.data_path = 'test/integration_test/data/integration-new-data-sample.csv'
        self.select_query = QueryHelper.query_result_formatter(
            'test/integration_test/test_query.sql/select_sample.sql')
        self.select_where = QueryHelper.query_result_formatter(
            'test/integration_test/test_query.sql/select_where_sample.sql')

        env_path = os.getcwd() + '/test/integration_test/.env'
        load_dotenv(dotenv_path=env_path, override=True)

    def test_can_extract_transfer_and_insert_data(self):
        ''' Passes test if data is extracted, transferd and inserted in database '''

        data_before_insertion = QueryHelper.query_result_formatter(
            DatabaseHelper.select(self.select_query))

        run(self.data_path)

        data_after_insertion = QueryHelper.query_result_formatter(
            DatabaseHelper.select(self.select_query))


if __name__ == "__main__":
    unittest.main()
