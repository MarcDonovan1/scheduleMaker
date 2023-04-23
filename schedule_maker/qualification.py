from datetime import datetime, timedelta

class Qualification:
    """
    Qualificaiton object used to represent a qualifcation

    Used to store different qualification types
    """

    def __init__(self, name: str, certification_date: datetime, expiry_date: datetime= None):
        self.name = name
        self.certification_date = certification_date
        self.expiry_date = expiry_date if expiry_date is not None else certification_date + timedelta(days=729)

    def is_expired(self, date_delta: datetime=None):
        """
        Returns a boolean if the qualification is expried form the date provided

        Args:
            date_delta: Date to compare to expiry date

        Return:
            True if the qualifcation is expired based on the date_delta, False otherwise
        """
        if date_delta is None:
            return self.expiry_date > datetime.today()
        return self.expiry_date > date_delta
