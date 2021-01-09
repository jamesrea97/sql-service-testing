''' Module helps sets environment for CLI '''

import os


def set_environment(path):
    ''' Sets required environment '''
    with open(path, 'r') as env_file:
        variables = env_file.read().splitlines()

        dict_var = {}
        for variable in variables:
            temp = variable.split('=')
            os.environ[temp[0]] = temp[1]
