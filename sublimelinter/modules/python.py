# -*- coding: utf-8 -*-
# python.py - sublimelint package for checking python files with flake8

import re

from .base_linter import BaseLinter, INPUT_METHOD_FILE

CONFIG = {
    'language': 'Python',
    'executable': 'flake8',
    'test_existence_args': '--version',
    'input_method': INPUT_METHOD_FILE,
}


class Linter(BaseLinter):
    def parse_errors(self, view, errors, lines, errorUnderlines, violationUnderlines, warningUnderlines, errorMessages, violationMessages, warningMessages):
        for line in errors.splitlines():
            match = re.match(r'^.+?:(?P<line>\d+):(?:(?P<offset>\d+):)?\s+(?P<error>.+)', line)

            if match:
                error, line, offset = match.group('error'), match.group('line'), match.group('offset')
                self.add_message(int(line), lines, error, errorMessages)
                if offset:
                    self.underline_range(view, int(line), int(offset), errorUnderlines)

    def get_lint_args(self, view, code, filename):
        settings = view.settings()
        flake8_builtins = ','.join(settings.get('flake8_builtins'))
        flake8_ignore = ','.join(settings.get('flake8_ignore'))
        return ('--builtins=%s' % flake8_builtins, '--ignore=%s' % flake8_ignore, filename)
