import logger

import transferer as transferer


def run(path):
    trans = transferer.Transferer()

    with open('test/sql/insert_users.sql') as query_file:
        query = query_file.read().replace('\n', '')

    if query:
        trans.transfer('test/data/sample.csv', query)


if __name__ == "__main__":
    pass
