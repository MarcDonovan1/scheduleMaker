from datetime import date

class Qualification:
    """
    Qualificaiton object used to represent a qualifcation

    Used to store different qualification types
    """

    def __init__(self, name: str, certification_date: date, expiry_date: date):
        self.name = name
        self.certification_date = certification_date
        self.expiry_date = expiry_date

    def is_expired(self, date_delta: date=date.today()):
        """
        Returns a boolean if the qualification is expried form the date provided

        Args:
            date_delta: Date to compare to expiry date

        Return:
            True if the qualifcation is expired based on the date_delta, False otherwise
        """
        return self.expiry_date>= date_delta
