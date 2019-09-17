import unittest

from DDERow import DDERow
from DDECell import DDECell


class TestDDERow(unittest.TestCase):
    def test_property_cells(self):
        cell = DDECell(2)
        cells = [DDECell(1), DDECell(2)]
        row = DDERow()
        row.cells = cells
        self.assertIsInstance(row.cells, list)
        self.assertEqual(row.cells[1].value, cell.value)

    def test_property_index(self):
        row = DDERow()
        row.index = 1
        self.assertEqual(row.index, 1)

    def test_add_cell(self):
        cell = DDECell(1)
        row = DDERow()
        row.add_cell(cell)
        rcell = row.cells[0]
        self.assertEqual(rcell, cell)

    def test_count(self):
        cell = DDECell(1)
        row = DDERow()
        row.add_cell(cell)
        self.assertEqual(row.count(), 1)

    def test_cell(self):
        cell = DDECell(2)
        row = DDERow()
        row.add_cell(DDECell(1))
        row.add_cell(cell)
        row.add_cell(DDECell(3))
        self.assertEqual(row.cell(1).value, cell.value)

    def test_cell_bigger_index(self):
        row = DDERow()
        row.add_cell(DDECell(1))
        row.add_cell(DDECell(2))
        row.add_cell(DDECell(3))
        self.assertEqual(row.cell(10), None)

    def test_cell_smaller_index(self):
        row = DDERow()
        row.add_cell(DDECell(1))
        row.add_cell(DDECell(2))
        row.add_cell(DDECell(3))
        self.assertEqual(row.cell(-1), None)

    def test_tostring(self):
        row = DDERow()
        row.add_cell(DDECell(1))
        row.add_cell(DDECell(2))
        self.assertEqual(row.tostring(), '1\t2\t')

    def test_tostring_separator(self):
        row = DDERow()
        row.add_cell(DDECell(1))
        row.add_cell(DDECell(2))
        self.assertEqual(row.tostring('|'), '1|2|')


if __name__ == '__main__':
    unittest.main()

