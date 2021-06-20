from configparser import ConfigParser
import logging
import psycopg2

from configobj import ConfigObj

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


# here we work with .ini files in order to have the configuration for our project
def config(filename='database.ini'):
    """
    This function returns all the databases with their config
    In .ini file for database configuration file
    :param filename:
    :return:
    """
    configs = {}  # this section holds all of the configs for all the databases
    parser = ConfigParser()
    parser.read(filename)
    data_bases = parser.sections()
    for data_base in data_bases:
        data_base_configs = parser.items(data_base)
        configs[data_base] = dict(data_base_configs)

    return configs


def connect(data_base_type='postgresql'):
    """
    Connects the user to appropriate database type base on the .ini file
    If there is no config info in .ini or wrong config info
    User get the proper message to fix the issue
    :param data_base_type:
    :return:
    """
    # by default we say that we wanna connect to a psql database
    configs = config()
    try:
        connection_params = configs[data_base_type]
        connection = psycopg2.connect(**connection_params)
    except KeyError:
        logging.warning(f'__CONFIG_ERROR__:CONFIG NOT FOUND FOR DATABASE |||{data_base_type}||| CHECK CONFIG FILE')
    except psycopg2.OperationalError:
        logging.fatal(f'__CONNECTION_ERROR__: CHECK DATABASE INFO IN CONFIG FILE ')

    else:
        return connection


def save_in_file():
    connection = connect()
    with connection.cursor() as cursor:
        cursor.execute("""SELECT column_name, data_type
                          -- From the system database information schema
                          FROM INFORMATION_SCHEMA.COLUMNS
                          -- For the customer table
                          WHERE table_name = 'person'""")
        for table in cursor:
            print(table)


save_in_file()




