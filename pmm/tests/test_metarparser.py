import unittest

from pmm.metarparser import MetarParser, NotAMetarException
from pmm.models import Metar


class MetarParserTest(unittest.TestCase):
    def setUp(self):
        self.metar_strings = (
            'LFRS 041600Z 12012MPS 090V150 1400 R04/P1500N R22/P1500U +SN BKN022 OVC050 M04/M07 Q1020 NOSIG 8849//91=',
            'METAR LFOV 201400Z 33008KT CAVOK 00/M01 Q1025',
            'this is not a valid METAR'
        )

    def test_process(self):
        parser = MetarParser(self.metar_strings[0])
        metar = parser.process()

        target_metar = Metar(
            'LFRS',
            self.metar_strings[0],
            2200,
            1400
        )

        self.assertEqual(metar, target_metar)

    def test_parse_icao(self):
        parser = MetarParser(self.metar_strings[0])
        icao = parser.parse_icao()
        self.assertEqual(icao, 'LFRS')

        parser = MetarParser(self.metar_strings[1])
        icao = parser.parse_icao()
        self.assertEqual(icao, 'LFOV')

    def test_raise_error_on_parse_icao(self):
        parser = MetarParser(self.metar_strings[2])
        with self.assertRaises(NotAMetarException):
            parser.parse_icao()

    def test_parse_ceiling_alt(self):
        parser = MetarParser(self.metar_strings[0])
        ceiling = parser.parse_ceiling_alt()
        self.assertEqual(ceiling, 2200)

        parser = MetarParser(self.metar_strings[1])
        ceiling = parser.parse_ceiling_alt()
        self.assertEqual(ceiling, 5000)

    def test_raise_error_on_parse_ceiling_alt(self):
        parser = MetarParser(self.metar_strings[2])
        with self.assertRaises(NotAMetarException):
            parser.parse_ceiling_alt()

    def test_parse_visibility(self):
        parser = MetarParser(self.metar_strings[0])
        visibility = parser.parse_visibility()
        self.assertEqual(visibility, 1400)

        parser = MetarParser(self.metar_strings[1])
        visibility = parser.parse_visibility()
        self.assertEqual(visibility, 9999)

    def test_raise_error_on_parse_visibility(self):
        parser = MetarParser(self.metar_strings[2])
        with self.assertRaises(NotAMetarException):
            parser.parse_visibility()