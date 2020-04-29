class Model():
    def select(self):
        """
        Gets all rows from the database as a list of lists.
        Row consists of name, street, city, state, zipcode, hours, phone, rating, review, foodtype, and date.
        :return: List of lists containing all rows of database
        """
        pass

    def insert(self, name, street, city, state, zipcode, hours, phone, rating, review, foodtype):
        """
        Inserts entry into database
        :param name: String
        :param street: String
        :param city: String
        :param state: String
        :param zipcode: String
        :param phone: String
        :param hours: String
        :param rating: String
        :param review: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass
