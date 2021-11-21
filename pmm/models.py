class Metar:
    """A Metar record for an Airport.

    Attributes:
        icao (str): Airport icao code
        full_text (str): Raw metar report
        ceiling_alt (int): Cloud ceiling altitude in feet
        visibility (int): Horizontal visibility in meters
        vmc_level (int<0, 5>): Visual meteorological conditions. A scale from 0 to 6.
    """
    icao: str
    text: str
    ceiling_alt: int
    visibility: int
    vmc_level: int

    def __eq__(self, other):
        """Used in unittests"""
        return self.icao == other.icao and \
               self.text == other.text and \
               self.ceiling_alt == other.ceiling_alt and \
               self.visibility == other.visibility and \
               self.vmc_level == other.vmc_level
