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
        self.select_query = QueryHelper.query_builder(
            'test/integration_test/test_query/select_sample.sql')
        self.select_where = QueryHelper.query_builder(
            'test/integration_test/test_query/select_where_sample.sql')

        self.insert_path = 'src/sql/insert_users.sql'

        # TODO Fix docker container to run on localhost
        # env_path = os.getcwd() + '/test/integration_test/.env'
        # load_dotenv(dotenv_path=env_path, override=True)

    def test_can_extract_transfer_and_insert_data(self):
        ''' Passes test if data is extracted, transferd and inserted in database '''

        data_before_insertion = QueryHelper.query_result_formatter(
            DatabaseHelper.select(self.select_query))

        run(self.insert_path, self.data_path)

        data_after_insertion = QueryHelper.query_result_formatter(
            DatabaseHelper.select(self.select_query))

        difference = list(QueryHelper.query_comparor(
            data_before_insertion, data_after_insertion))

        self.assertEqual(
            difference, [['John', 'Smith', '100', 'male', 'American']])


if __name__ == "__main__":
    unittest.main()
