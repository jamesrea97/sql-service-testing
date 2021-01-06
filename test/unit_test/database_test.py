""" Module unit tests Database class behaviour """

import unittest


class ShouldInsertData(unittest.TestCase):

    def setUp(self):
        ''' Sets up data path '''
        with open('test/sql/insert_users.sql') as query_file:
            self.query = query_file.read()

    def test_can_insert_data(self):
        ''' Passes test if data correctly inserted '''
        pass


if __name__ == "__main__":
    unittest.main()
