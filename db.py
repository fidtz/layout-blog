import psycopg2

connection = None
cursor = None

_cdatabase = #readfile for this
_chost = #readfile for this
_cport = #readfile for this
_cuser = #readfile for this
_cpassword = #readfile for this

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