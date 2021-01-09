import logger
import sys
import transferer as transferer
from environment import set_environment


def run(query_path, data_path, env_path=None):
    if env_path:
        set_environment(env_path)

    trans = transferer.Transferer()

    with open(query_path) as query_file:
        query = query_file.read().replace('\n', '')

    if query:
        trans.transfer(data_path, query)


if __name__ == "__main__":
    query_path = sys.argv[1]
    data_path = sys.argv[2]
    env_path = sys.argv[3]

    run(query_path, data_path, env_path)
