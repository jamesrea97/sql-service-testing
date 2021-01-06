""" Module unit tests Database class behaviour """
import context
import unittest
import src.database as database


class ShouldInsertData(unittest.TestCase):

    def setUp(self):
        ''' Sets up data path '''
        self.db = database.Database()
        with open('test/sql/insert_users.sql') as query_file:
            self.query = query_file.read().replace('\n', '')

    def test_can_insert_data(self):
        ''' Passes test if data correctly inserted '''
        self.db.insert(['James', 'Rea', 23, 'male', 'British'], self.query)


if __name__ == "__main__":
    unittest.main()
