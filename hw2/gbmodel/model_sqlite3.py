"""
A simple guestbook flask app.
ata is stored in a SQLite database that looks something like the following:
+------------+------------------+------------+----------------+
| Name       | Email            | signed_on  | message        |
+============+==================+============+----------------+
| John Doe   | jdoe@example.com | 2012-05-28 | Hello world    |
+------------+------------------+------------+----------------+
This can be created with the following SQL (see bottom of this file):
    create table guestbook (name text, email text, signed_on date, message);
"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from cartlist")
        except sqlite3.OperationalError:
            cursor.execute("create table cartlist (name text, phone text, signed_on date, review)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, phone, date, review 
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cartlist")
        return cursor.fetchall()

    def insert(self, name, phone, review):
        """
        Inserts entry into database
        :param name: String
        :param phone: String
        :param review: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'name':name, 'phone':phone, 'date':date.today(), 'review':review}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into guestbook (name, phone, signed_on, review) VALUES (:name, :phone, :date, :review)", params)

        connection.commit()
        cursor.close()
        return True
