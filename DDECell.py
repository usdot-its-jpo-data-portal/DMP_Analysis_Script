class DDECell:
    def __init__(self, value=None):
        self._value = value
        self._cell_type = None
        self._column_index = 0
        self._row_index = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def cell_type(self):
        return self._cell_type

    @cell_type.setter
    def cell_type(self, val):
        self._cell_type = val

    @property
    def column_index(self):
        return self._column_index

    @column_index.setter
    def column_index(self, val):
        self._column_index = val

    @property
    def row_index(self):
        return self._row_index

    @row_index.setter
    def row_index(self, val):
        self._row_index = val
