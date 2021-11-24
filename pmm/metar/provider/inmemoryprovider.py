from pmm.metar.provider import ProviderInterface, NotAValidIcaoCodeException
from pmm.metar.models import Metar
from pmm.metar.parser import Parser


class InMemoryProvider(ProviderInterface):
    """A dummy METAR provider, mainly used for unit and functional tests

       Only handles a pre defined list of 8 statics airport METARS
    """
    dummy_metars: dict = {
        "LFRS": "LFRS 231800Z AUTO 05012KT CAVOK 07/M02 Q1023 TEMPO 05015G25KT",
        "LFRI": "LFRI 231750Z 06004KT 0500 R24/1900N FG BKN002 BKN004 05/05 Q1029 TEMPO 0300 BR BKN001",
        "LFRZ": "LFRZ 231755Z AUTO VRB01KT 3200 BR OVC007 // / 05 / 04 Q1029 YLO",
        "LFOV": "LFOV 231800Z 03008G18KT 360V080 CAVOK 05 / 03 Q1027 NOSIG",
        "LFFI": "LFFI 231800Z AUTO 03006KT 9999 FEW025 OVC047 09/08 Q1029 TEMPO 3000 RA OVC002",
        "LFRN": "LFRN 231725Z AUTO 06007KT 6000 BR BKN002/// OVC004/// 05/05 Q1028 AMB",
        "LFJB": "LFJB 231725Z AUTO VRB01KT 1900 BR OVC047/// 08/08 Q1030 YLO",
        "LFOU": ""
    }

    def fetch_metar_by_icao_code(self, icao: str) -> Metar:
        if icao in self.dummy_metars:
            parser = Parser(self.dummy_metars[icao])
            return parser.process()

        raise NotAValidIcaoCodeException
