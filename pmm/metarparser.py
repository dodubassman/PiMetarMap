"""Parser takes metar text string and build a Metar object from it
"""
import re

from pmm.models import Metar


class MetarParser:
    def __init__(self, metar_as_text: str):
        self.metar_as_text = metar_as_text

    def process(self) -> Metar:
        metar = Metar()
        metar.icao = self.parse_icao()
        metar.text = self.metar_as_text
        metar.visibility = self.parse_visibility()
        metar.ceiling_alt = self.parse_ceiling_alt()
        metar.vmc_level = self.feed_vmc_level(metar.ceiling_alt, metar.visibility)
        return metar

    def parse_icao(self) -> str:
        search = re.search('((?!ETAR)[A-Z]{4}) ', self.metar_as_text)

        if search is None or type(search.group(1)) != str:
            raise NotAMetarException('No ICAO code')

        return search.group(1)

    def parse_ceiling_alt(self) -> int:
        # Ceiling And Visibility OK / No Significative Clouds = 5000ft
        if self.metar_as_text.find('CAVOK') > 0 or self.metar_as_text.find('NSC') > 0:
            return 5000

        search = re.findall('(FEW|SCT|BKN|OVC)(\\d{3})', self.metar_as_text)
        if search:
            ceiling = 5000
            for result in search:
                if int(result[1]) * 100 < ceiling:
                    ceiling = int(result[1]) * 100
            return ceiling

        raise NotAMetarException('Wrong cloud information')

    def parse_visibility(self) -> int:
        if self.metar_as_text.find('CAVOK') > 0:
            return 9999

        search = re.search(' (\\d{4}) ', self.metar_as_text)

        if search is None or type(search.group(1)) != str:
            raise NotAMetarException('Wrong visibility')

        return int(search.group(1))

    def feed_vmc_level(self, ceiling, visibility):
        if ceiling <= 200 or visibility <= 800:
            return 0
        elif ceiling <= 500 or visibility <= 1500:
            return 1
        elif ceiling <= 1000 or visibility <= 5000:
            return 2
        elif ceiling <= 2000 or visibility <= 8000:
            return 3
        elif ceiling <= 3000 or visibility < 9999:
            return 4
        else:
            return 5


class NotAMetarException(Exception):
    message = 'wrong metar format'