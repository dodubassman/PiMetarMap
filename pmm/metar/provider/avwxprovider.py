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
        resp = httpx.get("https://avwx.rest/api/metar/" + icao, headers={
            "Authorization": "BEARER " + bearer
        })

        if resp.content == b'':
            raise NoAvailableMetarDataException

        resp_dict = resp.json()
        if 'error' in resp_dict:
            raise NotAValidIcaoCodeException('Error with ICAO code: ' + icao + '. ' + resp_dict['error'])

        parser = Parser(resp_dict['raw'])
        return parser.process()
