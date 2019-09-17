import unittest

from DDEText import DDEText


class TestDDEText(unittest.TestCase):
    def test_property_value(self):
        dde_text = DDEText()
        dde_text.value = 'value'
        self.assertEqual(dde_text.value, 'value')

    def test_property_text(self):
        dde_text = DDEText()
        dde_text.text = 'text'
        self.assertEqual(dde_text.text, 'text')

    def test_property_id(self):
        dde_text = DDEText()
        dde_text.id = 'id'
        self.assertEqual(dde_text.id, 'id')

    def test_resolve_id(self):
        dde_text = DDEText()
        dde_text.text = 'A.01 This is the text.'
        id = dde_text.resolve_id()
        self.assertEqual(id, 'A.01')

    def test_resolve_id_no_text(self):
        dde_text = DDEText()
        dde_text.text = None
        id = dde_text.resolve_id()
        self.assertIsNone(id)

    def test_resolve_id_invalid_text(self):
        dde_text = DDEText()
        dde_text.text = 'This is the text'
        id = dde_text.resolve_id()
        self.assertIsNone(id)

    def test_tostring(self):
        dde_text = DDEText()
        dde_text.text = 'text'
        dde_text.value = 'value'
        dde_text.id = 'id'

        r = dde_text.tostring()
        s = '\t'
        e = '{}{}{}{}{}'.format(dde_text.id, s, dde_text.text, s, dde_text.value)
        self.assertEqual(r, e)

    def test_tostring_separator(self):
        dde_text = DDEText()
        dde_text.text = 'text'
        dde_text.value = 'value'
        dde_text.id = 'id'

        r = dde_text.tostring('|')
        s = '|'
        e = '{}{}{}{}{}'.format(dde_text.id, s, dde_text.text, s, dde_text.value)
        self.assertEqual(r, e)


if __name__ == '__main__':
    unittest.main()

