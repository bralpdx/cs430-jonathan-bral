class Model():
    def select(self):
        """
        Gets all rows from the database.
        Returns list of lists containing all
        rows of the database.
        """
        pass

    def insert(self, title, desc, prio):
        """
        Inserts individual entry into database.
        :param title: String
        :param desc: String
        :param prio: String
        """
        pass

    def delete_task(self, title, prio):
        """
        Deletes individual entry from database.
        :param title: String
        :param prio: String
        """
        pass
