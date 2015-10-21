import sqlite3
import names
import random

def open_conn_ret_cur(db_file):
    sqlite3.connect(db_file)
    return sqlite3.connect(db_file).cursor()

def count_table(cur,db_table):
    return list(cur.execute('''SELECT COUNT(*) FROM ''' + db_table))[0][0]
