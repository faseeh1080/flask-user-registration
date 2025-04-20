import mysql.connector
import click

from flask import current_app, g


def get_db():
    if "cnx" not in g:
        g.cnx = mysql.connector.connect(
            user="root",
            password="mysqlroot",
            host="127.0.0.1",
            database="flask_user_registration_app_database",
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


def init_db():
    cnx = mysql.connector.connect(user="root", password="mysqlroot", host="127.0.0.1")
    cursor = cnx.cursor()

    with current_app.open_resource("schema.sql") as f:
        schema_sql = f.read().decode("utf-8")

    for statement in schema_sql.split(";"):
        statement = statement.strip()
        if statement:
            cursor.execute(statement)

    cursor.close()
    cnx.close()


@click.command("init-db")
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
