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
        r'Error in module (?P<module>\S+).*Error at (\S+) line (?P<line>\d+), column (?P<col>\d+)(.+)\n\s*(?P<message>.+)See http'
    )
    re_flags = re.DOTALL
    multiline = True
    tempfile_suffix = '-'
    error_stream = util.STREAM_STDOUT

    def split_match(self, match):
        match, line, col, error, warning, message, near = (
            super().split_match(match)
        )
        module = match.groupdict()['module']

        return match, line, col, error, warning, module + " " + message, near
