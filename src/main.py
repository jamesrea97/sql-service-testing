import logger

import transferer as transferer


if __name__ == "__main__":
    trans = transferer.Transferer()

    with open('test/sql/insert_users.sql') as query_file:
        query = query_file.read().replace('\n', '')

    if query:
        trans.transfer('test/data/sample.csv', query)
