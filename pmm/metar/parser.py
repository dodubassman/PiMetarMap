"""Parser takes metar text string and build a Metar object from it
"""
import re

from pmm.metar.models import Metar


class Parser:
    def __init__(self, metar_as_text: str):
        self.metar_as_text = metar_as_text

    def process(self) -> Metar:
        metar = Metar(
            self.parse_icao(),
            self.metar_as_text,
            self.parse_ceiling_alt(),
            self.parse_visibility()
        )
        return metar

    def parse_icao(self) -> str:
        search = re.search('((?!ETAR)[A-Z]{4}) ', self.metar_as_text)

        if search is None or type(search.group(1)) != str:
            raise NotAMetarException('No ICAO code')

        return search.group(1)

    def parse_ceiling_alt(self) -> int:
        # we want the present weather, without tempo or becoming
        metar_without_tempo = self.metar_as_text.split('TEMPO')[0].split('BECMG')[0]

        # Ceiling And Visibility OK / No Significant Clouds = 5000ft
        if metar_without_tempo.find('CAVOK') > 0 or metar_without_tempo.find('NSC') > 0:
            return 5000

        # Sky not visible due to fog
        if metar_without_tempo.find('VV///') > 0:
            return 0

        search = re.findall('(FEW|SCT|BKN|OVC)(\\d{3})', metar_without_tempo)
        if search:
            ceiling = 5000
            for result in search:
                if result[0] == 'FEW' and int(result[1]) * 100 < 1000:
                    # FEW are considered only below 1000ft agl
                    ceiling = int(result[1]) * 100
                if int(result[1]) * 100 < ceiling:
                    ceiling = int(result[1]) * 100
            return ceiling

        raise NotAMetarException(self.parse_icao() + ': Wrong cloud information. ' + self.metar_as_text)

    def parse_visibility(self) -> int:
        # we want the present weather, without tempo
        metar_without_tempo = self.metar_as_text.split('TEMPO')[0]

        # Ceiling And Visibility OK = visibility > 10000m
        if metar_without_tempo.find('CAVOK') > 0:
            return 9999

        search = re.search(' (\\d{4}) ', metar_without_tempo)

        if search is None or type(search.group(1)) != str:
            raise NotAMetarException(self.parse_icao() + ': Wrong visibility')

        return int(search.group(1))


class NotAMetarException(Exception):
    message = 'wrong metar format'
