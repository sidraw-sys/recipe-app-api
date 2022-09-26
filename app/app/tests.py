from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    
    def test_add_func(self):
        res=calc.add(10,11)
        self.assertEqual(res,21)