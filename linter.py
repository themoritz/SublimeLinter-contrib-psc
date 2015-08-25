#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Moritz Drexl
# Copyright (c) 2015 Moritz Drexl
#
# License: MIT
#

"""This module exports the Psc plugin class."""

from SublimeLinter.lint import Linter, util
import re


class Psc(Linter):

    """Provides an interface to psc."""

    syntax = 'purescript'
    cmd = 'gulp make --@'
    regex = (
        r' "?(?P<module>\/\S+)"? .*line (?P<line>\d+), column (?P<col>\d+)(?P<message>.+)See http'
    )
    re_flags = re.DOTALL
    multiline = True
    tempfile_suffix = '-'
    error_stream = util.STREAM_STDOUT

    def split_match(self, match):
        match, line, col, error, warning, message, near = (
            super().split_match(match)
        )
        message = message.replace('\n', '')
        module = match.groupdict()['module']
        print(module, line, col, message)

        return match, line, col, error, warning, module + " " + message, near
