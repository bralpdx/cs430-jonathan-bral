"""
Data is stored in a Python list.  Returns a list of lists
  upon retrieval
"""
from datetime import date
from Model import Model

class model(Model):
    def __init__(self):
        self.guestentries = []

    def select(self):
        """
        Returns guestentries list of lists
        Each list in guestentries contains: name, email, date, message
        :return: List of lists
        """
        return self.guestentries

    def insert(self, name, phone, review):
        """
        Appends a new list of values representing new message into guestentries
        :param name: String
        :param phone: String
        :param review: String
        :return: True
        """
        params = [name, phone, date.today(), review]
        self.guestentries.append(params)
        return True
