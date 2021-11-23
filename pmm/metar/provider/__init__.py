from abc import ABC, abstractmethod

from pmm.metar.models import Metar


class ProviderInterface(ABC):
    def fetch_metar_by_icao_code(self, icao: str) -> Metar:
        pass


class NotAValidIcaoCodeException(Exception):
    message = "Provided ICAO code doesn't exist"
