""" Module unit tests Extractor class behaviour """

import unittest

import context
import src.extractor as extractor


class ShouldExtractData(unittest.TestCase):

    def setUp(self):
        ''' Sets up data path '''
        self.data_path = '../data/sample.csv'

    def test_can_extract_data(self):
        ''' Passes test if data correctly extracted '''
        data = extractor.Extractor()
    