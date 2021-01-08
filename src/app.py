import logger

import transferer as transferer


def run(query_path, data_path):
    trans = transferer.Transferer()

    with open(query_path) as query_file:
        query = query_file.read().replace('\n', '')

    if query:
        trans.transfer(data_path, query)


if __name__ == "__main__":
    pass
