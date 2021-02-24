import unittest
from read_animals import check_parents_index_range
from read_animals import check_parents_index_type

class TestReadAnimals(unittest.TestCase):

    def test_check_parents_index_range(self):
        self.assertEqual(check_parents_index_range(2,17),'Parent indices: 2 and 17 range pass')
        self.assertEqual(check_parents_index_range(2,22),'Parent 2 index: 22 range FAIL')
        self.assertEqual(check_parents_index_range(-1,19),'Parent 1 index: -1 range FAIL')
        self.assertEqual(check_parents_index_range(-1,22),'Parent 1 index: -1 range FAIL')

    def test_check_parents_index_type(self):
        self.assertEqual(check_parents_index_type('2'),'Parent index: 2 type pass')
        self.assertEqual(check_parents_index_type('f'),'Parent index: f type FAIL') # sys.argv always stores as str so bools and lists need not be tested

if __name__ == '__main__':
    unittest.main()

