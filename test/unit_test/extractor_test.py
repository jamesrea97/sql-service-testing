""" Module unit tests Extractor class behaviour """

import unittest

import context
import src.extractor as extractor


class ShouldExtractData(unittest.TestCase):

    def setUp(self):
        ''' Sets up data path '''
        self.data_path = 'test/data/sample.csv'

    def test_can_extract_data(self):
        ''' Passes test if data correctly extracted '''
        data = extractor.Extractor.extract(self.data_path)

        self.assertEqual(len(data), 3)
        self.assertEqual(
            data[2], ['Bella', 'Martin', '3', 'female', 'Spanish'])


if __name__ == "__main__":
    unittest.main()
