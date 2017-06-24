import unittest
from unittest.mock import patch
from model import Model
import test_helpers

class TestUserClass(unittest.TestCase):

    @patch('datetime.datetime.now', side_effect=test_helpers.date)
    def test_add_record(self, add_record):
        model = Model("none")
        model.add_record(220)
        self.assertEqual(model.records, [{"pressure": 220,"date": "DATE"}])
        
if __name__ == "__main__":
    unittest.main()
