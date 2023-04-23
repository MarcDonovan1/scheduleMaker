import unittest
from schedule_maker.qualification import Qualification
from datetime import datetime, timedelta

class TestQualification(unittest.TestCase):

    def test__init__(self):
        qual = Qualification("NLS", datetime(2022,2,20))

        self.assertEqual(qual.name,"NLS")
        self.assertEqual(qual.certification_date, datetime(2022,2,20))
        self.assertEqual(qual.expiry_date, datetime(2024,2,19))

        qual = Qualification("NLS", datetime(2022,2,20), datetime(2023,2,20))

        self.assertEqual(qual.name,"NLS")
        self.assertEqual(qual.certification_date, datetime(2022,2,20))
        self.assertEqual(qual.expiry_date, datetime(2023,2,20))

    def test_is_expired(self):

        qual = Qualification("NLS", datetime(1999,1,1))
        self.assertFalse(qual.is_expired())

        qual.expiry_date = datetime.today() + timedelta(days=1)
        self.assertTrue(qual.is_expired())

        self.assertTrue(qual.is_expired(datetime.today()))

if __name__ == "__main__":
    unittest.main()