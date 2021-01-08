""" Module contains QueryHelper, a helper for testing generating querys for testing DB behaviour """


class QueryHelper:

    @classmethod
    def query_result_formatter(cls, data):
        ''' Formats data in a readable manner for test '''
        return [r[0].replace('(', '').replace(')', '').split(',') for r in data]

    @classmethod
    def query_builder(cls, path):
        ''' Builds query from file '''
        with open(path, 'r') as query_file:
            return query_file.read()

    @classmethod
    def query_comparor(cls, query_before, query_after):
        ''' Returns a list of elements present in query_after but not in query_before  '''
        result = []
        for entry in query_after:
            if entry not in query_before:
                result.append(entry)
        return result
