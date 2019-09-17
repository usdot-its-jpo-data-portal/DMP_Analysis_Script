import re


class DDEText:
    def __init__(self):
        self._value = None
        self._text = None
        self._id = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, val):
        self._text = val

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        self._id = val

    def resolve_id(self):
        if self._text is None:
            return None

        lst = re.findall(r'[A0].[0-9][0-9]', self._text)
        if lst is None or len(lst) == 0:
            return None

        id = lst[0]
        self._id = id
        self._text = self._text[len(id):]
        return id

    def tostring(self, separator='\t'):
        if self._text is None:
            return None

        id = self._id if self._id is not None else ''
        return '{}{}{}{}{}'.format(id, separator, self._text, separator, self._value)
