import unittest
from schedule_maker.shift import Shift
from datetime import datetime

class TestShift(unittest.TestCase):

    def test__init__(self):
        config = {
            "start_time" : "08:30",
            "end_time" : "10:30"
        }
        shift = Shift(config)

        self.assertEqual(str(shift.start_time),"08:30:00")
        self.assertEqual(str(shift.end_time),"10:30:00")
        self.assertEqual(shift.type,"GUARD")
        self.assertEqual(
            shift.staff_needed,{
                "supervisors": 1,
                "guards": 1,
                "instructors": 0        
            }
        )

    def test_str(self):
        config = {
            "start_time" : "06:00",
            "end_time" : "08:30"
        }
        shift = Shift(config)

        self.assertEqual(str(shift),"06:00-08:30")

if __name__ == "__main__":
    unittest.main()