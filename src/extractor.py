""" Module contains Extractor class used to retrieve information from .csv files """


class Extractor:

    @classmethod
    def extract(cls, path):
        ''' Extracts data from .csv file '''
        result = []
        with open(path, 'r') as data_file:

            data = data_file.read().splitlines()

            for line in data:
                result.append(line.split(','))
        return result
