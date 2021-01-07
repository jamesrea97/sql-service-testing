""" Module unit tests Extractor class behaviour """

import unittest

import context
import test_environment

import extractor as extractor


class ShouldExtractData(unittest.TestCase):

    def setUp(self):
        ''' Sets up data path '''
        self.data_path = 'test/data/sample.csv'

    def test_can_extract_data(self):
        ''' Passes test if data correctly extracted '''
        data = extractor.Extractor.extract(self.data_path)

        self.assertEqual(len(data), 1)
        self.assertEqual(
            data[0], ['Bella', 'Martin', '3', 'female', 'Spanish'])


if __name__ == "__main__":
    unittest.main()
