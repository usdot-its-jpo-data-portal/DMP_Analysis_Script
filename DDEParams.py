import argparse
import os

class DDEParams:
    def __init__(self):
        self._path_name = None
        self._is_directory = False
        self._output = None
        self._is_valid = True
        self._message = None
        self._detailed = False

    @property
    def path_name(self):
        return self._path_name

    @path_name.setter
    def path_name(self, value):
        self._path_name = value

    @property
    def is_directory(self):
        return self._is_directory

    @is_directory.setter
    def is_directory(self, value):
        self._is_directory = value

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        self._output = value

    @property
    def is_valid(self):
        return self._is_valid;

    @is_valid.setter
    def is_valid(self, value):
        self._is_valid = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def detailed(self):
        return self._detailed

    @detailed.setter
    def detailed(self, value):
        self._detailed = value

    def __str__(self):
        s = 'DDEParams(path_name = {}, is_directory = {}, output = {}, detailed = {})'.format(
            self._path_name,
            self._is_directory,
            self._output,
            self._detailed
        )
        return s

    def _argument_parser(self, args):
        parser = argparse.ArgumentParser(description="DOT Document Evaluation Parser")
        parser.add_argument('-o', '--output', help='Output directory')
        parser.add_argument('-d', '--detailed', action='store_true', default=False, help='Detailed report')
        parser.add_argument('PATH', help='Input DOCX(s) file(s) to process')

        params = parser.parse_args(args)

        return params

    def _validate_cmd_params(self, args):
        try:
            params = self._argument_parser(args)

            is_file = os.path.isfile(params.PATH)
            if is_file:
                self._is_directory = False
                self._is_valid = True
            else:
                if os.path.isdir(params.PATH):
                    self._is_directory = True
                    self._is_valid = True
                else:
                    self._is_valid = False
                    print('Error: PATH not found.')
                    params.print_help()

            self._path_name = params.PATH
            self._output = params.output
            self._detailed = params.detailed

        except:
            self._is_valid = False

    def validate_params(self, args):
        self._validate_cmd_params(args)
