import unittest

from pmm.metar.provider import NotAValidIcaoCodeException
from pmm.metar.provider.inmemoryprovider import InMemoryProvider
from pmm.metar.models import Metar


class InMemoryProviderTest(unittest.TestCase):
    def test_fetch_metar_by_icao_code(self):
        provider = InMemoryProvider()
        metar = provider.fetch_metar_by_icao_code('LFRS')

        self.assertIs(type(metar), Metar)
        self.assertEqual(metar.icao, 'LFRS')

    def test_raise_error_on_wrong_icao_code(self):
        provider = InMemoryProvider()
        with self.assertRaises(NotAValidIcaoCodeException):
            provider.fetch_metar_by_icao_code('not-an-icao-code')
