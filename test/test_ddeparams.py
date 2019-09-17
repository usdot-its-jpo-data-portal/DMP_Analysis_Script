import unittest
import os

from DDEParams import DDEParams


class TestDDEParams(unittest.TestCase):
    def test_property_path_name(self):
        params = DDEParams()
        params.path_name = 'path'
        self.assertEqual(params.path_name, 'path')

    def test_property_is_directory(self):
        params = DDEParams()
        params.is_directory = True
        self.assertEqual(params.is_directory, True)

    def test_property_output(self):
        params = DDEParams()
        params.output = 'output'
        self.assertEqual(params.output, 'output')

    def test_property_is_valid(self):
        params = DDEParams()
        params.is_valid = False
        self.assertEqual(params.is_valid, False)

    def test_property_detailed(self):
        params = DDEParams()
        params.detailed = True
        self.assertEqual(params.detailed, True)

    def test__argument_parser_empty(self):
        params = []
        dde_params = DDEParams()
        p = None
        try:
            p = dde_params._validate_cmd_params(params)
        except:
            p = None

        self.assertIsNone(p)

    def test__argument_parser_PATH(self):
        params = ['PATH']
        dde_params = DDEParams()
        p = None
        try:
            p = dde_params._argument_parser(params)
        except:
            p = None

        self.assertTrue(p is not None)
        self.assertEqual(p.PATH, 'PATH')

    def test__argument_parser_detailed(self):
        params = ['-d', 'PATH']
        dde_params = DDEParams()
        p = None
        try:
            p = dde_params._argument_parser(params)
        except:
            p = None

        self.assertTrue(p is not None)
        self.assertTrue(p.detailed)

    def test__argument_parser_output(self):
        params = ['-o', 'OUTPUT', 'PATH']
        dde_params = DDEParams()
        p = None
        try:
            p = dde_params._argument_parser(params)
        except:
            p = None

        self.assertTrue(p is not None)
        self.assertEqual(p.output, 'OUTPUT')

    def test__argument_parser_no_path(self):
        params = ['-o', 'OUTPUT', '-d']
        dde_params = DDEParams()
        p = None
        try:
            p = dde_params._argument_parser(params)
        except:
            p = None

        self.assertTrue(p is None)

    def test__validate_cmd_params(self):
        params = ['-o', 'OUTPUT', os.curdir]
        dde_params = DDEParams()
        p = None
        try:
            dde_params._validate_cmd_params(params)
        except:
            p = None

        self.assertTrue(dde_params.is_valid)
        self.assertEqual(dde_params.path_name, os.curdir)
        self.assertEqual(dde_params.detailed, False)
        self.assertEqual(dde_params.output, 'OUTPUT')


if __name__ == '__main__':
    unittest.main()
