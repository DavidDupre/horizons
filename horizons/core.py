from horizons.parse_table import parse_table
import logging
import re
from telnetlib import Telnet


logger = logging.getLogger(__name__)


class HorizonsException(Exception):
    pass


class Horizons:
    TIMEOUT = 4  # seconds

    def __init__(self):
        # connect
        self.tn = Telnet('horizons.jpl.nasa.gov', 6775)
        self._expect('Horizons> ')
        logger.info('connected to HORIZONS')

        # disable scrolling
        self._write('PAGE')
        self._expect('Output PAGING toggled OFF.')
        self._expect('Horizons> ')
        logger.debug('disabled output paging')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._write('X')
        self.tn.close()
        return True

    def _write(self, command):
        self.tn.write(command.encode('utf-8'))
        self.tn.write(b'\r\n')

    def _expect(self, expected):
        expected = str.encode(re.escape(expected))
        r = self.tn.expect([expected], Horizons.TIMEOUT)
        if r[1] is None:
            raise HorizonsException(f'Unexpected output: {r[2]}')
        return r[2].decode('utf-8')

    def get_major_bodies(self):
        self._write('MB')
        output = self._expect('Select ... [F]tp, [M]ail, [R]edisplay, ?, <cr>: ')
        lines = output.split('\r\n')

        # trim the output to just the table
        last_line_index = next(i for (i, line) in enumerate(lines) if line.isspace())
        lines = lines[4:last_line_index]

        # parse the output as a table
        return parse_table(lines)
