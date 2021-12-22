import json

from pmm.metar.provider import ProviderInterface, NotAValidIcaoCodeException, NoAvailableMetarDataException
from pmm.metar.models import Metar
from pmm.metar.parser import Parser
from pmm import settings
import httpx


class AvwxProvider(ProviderInterface):
    """A METAR provider using AVWX, Aviation Weather REST API
       Needs a user account and a bearer token. See settings.
    """

    def fetch_metar_by_icao_code(self, icao: str) -> Metar:
        if icao == '':
            raise NotAValidIcaoCodeException('Empty icao code')

        # API Call
        bearer = settings.AVWX_WEATHER_API['bearer']
        try:
            resp = httpx.get("https://avwx.rest/api/metar/" + icao, headers={
                "Authorization": "BEARER " + bearer
            }, timeout=10.0)
        except httpx.ReadTimeout:
            raise NoAvailableMetarDataException('A timeout occured while fetching metar data')

        if resp.content == b'':
            raise NoAvailableMetarDataException

        try:
            resp_dict = resp.json()
        except json.decoder.JSONDecodeError:
            raise NoAvailableMetarDataException('Error while parsing METAR JSON data')

        if 'raw' not in resp_dict:
            raise NoAvailableMetarDataException

        if 'error' in resp_dict:
            raise NotAValidIcaoCodeException('Error with ICAO code: ' + icao + '. ' + resp_dict['error'])

        parser = Parser(resp_dict['raw'])
        return parser.process()
