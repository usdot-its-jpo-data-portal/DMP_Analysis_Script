import unittest

from DDECell import DDECell
from DDERow import DDERow
from DDETable import DDETable


class TestDDETable(unittest.TestCase):
    def test_property_rows(self):
        row = DDERow()
        cell = DDECell(1)
        row.add_cell(cell)
        rows = [row]

        dde_table = DDETable()
        dde_table.rows = rows

        self.assertEqual(len(dde_table.rows), 1)

    def test_property_index(self):
        dde_table = DDETable()
        dde_table.index = 1
        self.assertEqual(dde_table.index, 1)

    def test_property_name(self):
        dde_table = DDETable()
        dde_table.name = 'name'
        self.assertEqual(dde_table.name, 'name')

    def test_add_row(self):
        row = DDERow()
        cell = DDECell(1)
        row.add_cell(cell)

        dde_table = DDETable()
        dde_table.add_row(row)

        self.assertEqual(len(dde_table.rows), 1)

    def test_row_count(self):
        row = DDERow()
        cell = DDECell(1)
        row.add_cell(cell)

        dde_table = DDETable()
        dde_table.add_row(row)

        self.assertEqual(dde_table.row_count(), 1)

    def test_row(self):
        row = DDERow()
        cell = DDECell(1)
        row.add_cell(cell)

        dde_table = DDETable()
        dde_table.add_row(row)

        self.assertEqual(dde_table.row(0).cell(0).value, 1)

    def test_row_bigger_index(self):
        row = DDERow()
        cell = DDECell(1)
        row.add_cell(cell)

        dde_table = DDETable()
        dde_table.add_row(row)

        self.assertIsNone(dde_table.row(10))

    def test_row_negative_index(self):
        row = DDERow()
        cell = DDECell(1)
        row.add_cell(cell)

        dde_table = DDETable()
        dde_table.add_row(row)

        self.assertIsNone(dde_table.row(-1))

if __name__ == '__main__':
    unittest.main()

