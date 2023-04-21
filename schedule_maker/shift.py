
from datetime import datetime

class Shift:
    """
    Base class used to represent a shift, this contains important such as

    Start and end time
    Type of shift
    Number of staff needed for shift
    """

    staff_on_shift = {
        "super": [],
        "guards": [],
        "instructors": []
    }

    staff_needed = {
        "supervisors": 0,
        "guards": 0,
        "instructors": 0
    }

    def __init__(self,config):
        self.start_time = datetime.strptime(config["start_time"],"%H:%M").time()
        self.end_time = datetime.strptime(config["end_time"],"%H:%M").time()
        self.type = config["type"] if "type" in config else "GUARD"
        self.staff_needed["supervisors"] = config["supervisors_needed"] if "supervisors_needed" in config else 1
        self.staff_needed["guards"] = config["guards_needed"] if "guards_needed" in config else 1
        self.staff_needed["instructors"] = config["instructors_needed"] if "instructors_needed" in config else 0

    def add_staff_to_shift(self, name: str, role: str):
        if len(self.staff_needed[role]) >= self.staff_needed[role]:
            raise ValueError(f"No more staff need for role {role}")
        self.staff_on_shift.append(name)

    def __str__(self):
        print(self.start_time)
        return self.start_time.isoformat(timespec="minutes") + "-" + self.end_time.isoformat(timespec="minutes")
