""" Module contains Transferer that drives the extraction of data from .cv and upload of data to db """
import logging
import src.extractor as extractor
import src.database as database


class Transferer:

    def __init__(self, db=None):
        ''' Initializes Database '''
        if db:
            self.db = db
        else:
            self.db = database.Database()

    def transfer(self, data_path, db_query):
        ''' Transfers data from data_path to self.db using db_query '''
        logging.info('Extracting data from {} ...'.format(data_path))
        data = extractor.Extractor.extract(data_path)

        logging.info('Inserting data into PostgreSQL db ...')
        try:
            self.db.insert(data, db_query)
        except:
            logging.error('Successfully added to PostgreSQL db ...')
        else:
            logging.info('Successfully added to PostgreSQL db ...')
