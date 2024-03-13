import unittest
from src.calendar_module.utils import calendar_module

class CalendarModule(unittest.TestCase):
        def test_testcase1(self):
            self.assertEqual(calendar_module(),'SUNDAY')

        def test_testcase2(self):
            self.assertEqual(calendar_module(), 'MONDAY')

        def test_testcase3(self):
            self.assertEqual(calendar_module(), 'WEDNESDAY')