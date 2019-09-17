import unittest

from DDECell import DDECell


class TestDDECell(unittest.TestCase):
    def test_property_value(self):
        cell = DDECell()
        cell.value = 'test'
        self.assertEqual(cell.value, 'test')

    def test_property_cell_type(self):
        cell = DDECell()
        cell.cell_type = 'type'
        self.assertEqual(cell.cell_type, 'type')

    def test_property_column_index(self):
        cell = DDECell()
        cell.column_index = 1
        self.assertEqual(cell.column_index, 1)

    def test_property_row_index(self):
        cell = DDECell()
        cell.row_index = 1
        self.assertEqual(cell.row_index, 1)


if __name__ == '__main__':
    unittest.main()

