""" Module contains QueryHelper, a helper for testing generating querys for testing DB behaviour """


class QueryHelper:

    @classmethod
    def query_result_formatter(cls, data):
        ''' Formats data in a readable manner for test '''
        # TODO
        pass

    @classmethod
    def query_builder(cls, path):
        ''' Builds query from file '''
        with open(path, 'r') as query_file:
            return query_file.read()
