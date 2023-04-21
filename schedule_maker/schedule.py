from schedule_maker.shift import Shift

class Schedule:
    """
    Base class to make a schedule object, this will hold the persons availability 
    """

    def __init__(self):
        self.schedule_week = {
            "Sunday": [],
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
        }

    def add_slot(
        self,
        date: str,
        shift: Shift):
        """
        This method is used to create a shift in the schedule
        """
        if date in self.schedule_week:
            self.schedule_week[date].append(shift)
            return True
        return False
    
    def show_schedule(self):
        for day in self.schedule_week:
            for shift in self.schedule_week[day]:
                print(shift)
