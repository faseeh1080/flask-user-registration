import mysql.connector

from flask import current_app, g


def get_db():
    if "cnx" not in g:
        g.cnx = mysql.connector.connect(
            user="scott", password="password", host="127.0.0.1", database="employees"
        )
        g.cursor = g.cnx.cursor()
    return g.cursor


def close_db(e=None):
    cursor = g.pop("cursor", None)
    cnx = g.pop("cnx", None)

    if cursor is not None:
        cursor.close()

    if cnx is not None:
        cnx.close()
