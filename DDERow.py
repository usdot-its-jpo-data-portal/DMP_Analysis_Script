class DDERow:
    def __init__(self):
        self._cells = []
        self._index = 0

    @property
    def cells(self):
        return self._cells

    @cells.setter
    def cells(self, val):
        self._cells = val

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, val):
        self._index = val

    def add_cell(self, cell):
        self._cells.append(cell)

    def count(self):
        return len(self._cells)

    def cell(self, index):
        if (index >= len(self._cells)) or (index < 0):
            return None

        return self._cells[index]


    def tostring(self, separator='\t'):
        result = ''
        if len(self._cells) <= 0:
            return result

        for cell in self._cells:
            result += '{}{}'.format(cell.value, separator)

        return result
