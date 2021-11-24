import unittest

from pmm.metar.provider import NotAValidIcaoCodeException, NoAvailableMetarDataException
from pmm.metar.provider.avwxprovider import AvwxProvider
from pmm.metar.models import Metar


class AvwxProviderTest(unittest.TestCase):
    def test_fetch_metar_by_icao_code(self):
        provider = AvwxProvider()
        metar = provider.fetch_metar_by_icao_code('LFRS')

        self.assertIs(type(metar), Metar)
        self.assertEqual(metar.icao, 'LFRS')

    def test_raise_error_on_wrong_icao_code(self):
        provider = AvwxProvider()
        with self.assertRaises(NotAValidIcaoCodeException):
            provider.fetch_metar_by_icao_code('not-an-icao-code')

    def test_raise_error_on_no_data_available(self):
        provider = AvwxProvider()
        with self.assertRaises(NoAvailableMetarDataException):
            provider.fetch_metar_by_icao_code('LFFI')
