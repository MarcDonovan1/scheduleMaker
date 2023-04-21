
from datetime import time
import abc

class Shift:
    """
    Base class used to represent a shift, this contains info such as
        1. Time of the shift
    """

    def __init__(self,start_time: time,end_time: time):
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return self.start_time.isoformat(timespec="minutes") + "-" + self.end_time.isoformat(timespec="minutes")

