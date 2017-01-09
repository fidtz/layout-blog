import psycopg2
from os.path import expanduser
import configparser

connection = None
cursor = None

home = expanduser("~")
auth = configparser.ConfigParser()
auth.read(home + '/.dbpy')

_cdatabase = auth['auth']['_cdatabase']
_chost = auth['auth']['_chost']
_cport = auth['auth']['_cport']
_cuser = auth['auth']['_cuser']
_cpassword = auth['auth']['_cpassword']

def _getconnection():
    global connection
    if not connection:
        connection = psycopg2.connect(dbname=_cdatabase, host=_chost, port=_cport , user=_cuser, password=_cpassword)
    return connection

def _getcursor():
    global connection
    global cursor
    _getconnection()
    if not cursor:
        cursor = connection.cursor()
    return cursor

_getcursor()

def close():
    global connection
    global cursor
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    return 'closed'

# List of stuff accessible to importers of this module. Just in case
__all__ = ['connection', 'cursor','close']