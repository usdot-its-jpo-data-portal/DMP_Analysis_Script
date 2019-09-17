class DDETable:
    def __init__(self):
        self._rows = []
        self._index = 0
        self._name = None

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, val):
        self._rows = val

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, val):
        self._index = val

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    def add_row(self, row):
        self._rows.append(row)

    def row_count(self):
        return len(self._rows)

    def row(self, index):
        if (index >= len(self._rows)) or (index < 0):
            return None

        return self._rows[index]


    def tostring(self, separator='\t'):
        result = ''
        if len(self._rows) <= 0:
            return result

        for row in self._rows:
            result += '{}{}'.format(row.tostring(separator), '\n')

        return result

