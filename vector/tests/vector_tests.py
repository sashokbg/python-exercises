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

    def test_2Dvector_length(self):
        vector1 = Vector([5,2])

        self.assertEqual(vector1.magnitude(), 5.385164807134504)

    def test_3Dvector_length(self):
        vector = Vector([3, 2, 5])

        self.assertEqual(vector.magnitude(), 6.164414002968976) 
