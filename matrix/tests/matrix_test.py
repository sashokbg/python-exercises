import unittest
from matrix.matrix import Matrix

class TestMatrix(unittest.TestCase):

    def test_create_matrix(self):
        m = Matrix(3)
        self.assertEqual(m.columns_size(), m.rows_size())
        self.assertEqual(m.columns_size(), 3)
