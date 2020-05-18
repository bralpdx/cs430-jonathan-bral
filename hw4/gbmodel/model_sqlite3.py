"""
A simple guestbook flask app.
ata is stored in a SQLite database that looks something like the following:
+------------+------------------+------------+------------------------------------------------------------------------------------+
| Name       |     Street       |   City     |State | Zipcode |    Hours   |    Phone      | Rating |   Review   |   posted_on    |
+============+==================+============+------------------------------------------------------------------------------------+
| John Doe   | 11111 NW Main St.| Portland   |  OR  | 97035   | 8am - 10pm | 503-867-5309  |   3/5  |   was okay |   2012-05-28   |
+------------+------------------+------------+------------------------------------------------------------------------------------+
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
            cursor.execute(
                    "create table cartlist (name text, street text, city text,"
                    " state text, zipcode text, hours text, phone text,"
                    " rating text, review, foodtype text, posted_on date)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, street, city, state, zipcode, hours, phone, rating, review, foodtype, date
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cartlist")
        return cursor.fetchall()

    def insert(self, name, street, city, state, zipcode, hours, phone, rating, review, foodtype):
        """
        Inserts entry into database
        :param name: String
        :param street: String
        :param city: String
        :param state: String
        :param zipcode: String
        :param hours: String
        :param phone: String
        :param rating: String
        :param review: String
        :param foodtype: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'name':name, 'street':street, 'city':city, 'state':state,
                'zipcode':zipcode, 'hours':hours, 'phone':phone, 'rating':rating,
                'review':review, 'foodtype':foodtype, 'date':date.today()}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute(
                "insert into cartlist (name, street, city, state, zipcode, hours, phone, rating, review, foodtype, posted_on)"
                "VALUES (:name, :street, :city, :state, :zipcode, :hours, :phone, :rating, :review, :foodtype, :date)", params)

        connection.commit()
        cursor.close()
        return True
