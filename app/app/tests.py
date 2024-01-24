"""
Sample Test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests (SimpleTestCase):
    """ Test calc module"""
    
    def test_add_number(self):
        """Test add number togetehr"""
        res=  calc.add(5,6)
        self.assertEqual(res, 11)
        

    def test_substract(self):
        """Test value for substraction"""
        res =  calc.subtract(10, 8)
        self.assertEqual(res, 2)