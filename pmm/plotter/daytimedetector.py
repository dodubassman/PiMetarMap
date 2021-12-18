from dataclasses import dataclass

from astral.geocoder import database, lookup
from astral.sun import sun


@dataclass
class DaytimeDetector:
    city: str

    def is_daytime(self, utc_datetime) -> bool:
        city = lookup(self.city, database())

        sun_position = sun(city.observer, date=utc_datetime)

        if utc_datetime < sun_position['dawn'] or utc_datetime > sun_position['dusk']:
            # Nighttime
            return False
        else:
            # Daytime
            return True
