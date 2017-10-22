import unittest
from vector.vector import Vector

class TestVector(unittest.TestCase):
    
    def test_create(self):
        vector = Vector([-3, 2, 0])
        
        self.assertEqual(vector.elements,[-3, 2, 0])

    def test_add_number(self):
        vector = Vector([-3, 2, 0])

        vector.add(3)

        self.assertEqual(vector.elements, [0, 5, 3])

    def test_add_vector(self):
        vector1 = Vector([-3, 2, 5])
        vector2 = Vector([5, -4, 4])

        self.assertEqual(vector1.add_vector(vector2).elements, [2, -2, 9])
