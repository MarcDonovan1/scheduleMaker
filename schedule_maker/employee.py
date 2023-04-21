from schedule_maker.qualification import Qualification
from schedule_maker.schedule import Schedule
class Employee:
    """
    Base class to define what an employee is and attributes they can have
    """

    _valid_levels = ["INSTRUCTOR", "GUARD","SENIOR GUARD", "SUPERVISOR"]
    def __init__(self, name: str, level: str, schedule: Schedule, qualification: list[Qualification]):

        self.name = name
        if level.upper() not in self._valid_levels:
            raise KeyError(f"{level} is not a valid level")
        self.level = level
        self.schedule = schedule
        self.qualifications = qualification if isinstance(qualification, list) else [qualification]

    def is_available(self, day: str, shift: str):
        """
        Use to determine if an employee is able to work a current shift
        """
        return False

    def is_qualified(self):
        """
        Method used to determine if an employees qualifications are current 
        """
        expired_quals = []
        for qual in self.qualifications:
            if qual.is_expired():
                expired_quals.append(qual)
        if len(expired_quals) > 0:
            return expired_quals
        return True
