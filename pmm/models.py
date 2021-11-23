from dataclasses import dataclass


@dataclass
class Metar:
    """A Metar record for an Airport.
    Attributes:
        icao (str): Airport icao code
        full_text (str): Raw metar report
        ceiling_alt (int): Cloud ceiling altitude in feet
        visibility (int): Horizontal visibility in meters
        vmc_level (int<0, 5>): Visual meteorological conditions. A scale from 0 to 5.
    """
    icao: str
    text: str
    ceiling_alt: int
    visibility: int

    @property
    def vmc_level(self) -> int:
        if self.ceiling_alt <= 200 or self.visibility <= 800:
            return 0
        elif self.ceiling_alt <= 500 or self.visibility <= 1500:
            return 1
        elif self.ceiling_alt <= 1000 or self.visibility <= 5000:
            return 2
        elif self.ceiling_alt <= 2000 or self.visibility <= 8000:
            return 3
        elif self.ceiling_alt <= 3000 or self.visibility < 9999:
            return 4
        else:
            return 5

    def __eq__(self, other):
        """Used in unittests"""
        return self.icao == other.icao and \
               self.text == other.text and \
               self.ceiling_alt == other.ceiling_alt and \
               self.visibility == other.visibility and \
               self.vmc_level == other.vmc_level
