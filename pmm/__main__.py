from typing import Dict

from pmm import settings
from pmm.apithrottler import ApiThrottler
from pmm.metar.provider import ProviderInterface, NoAvailableMetarDataException, NotAValidIcaoCodeException
from pmm.metar.parser import NotAMetarException
from pmm.metar.provider.avwxprovider import AvwxProvider
from pmm.plotter import PlotterInterface, Plot
from pmm.plotter.neopixelplotter import NeoPixelPlotter


def main(provider: ProviderInterface, plotter: PlotterInterface, throttler: ApiThrottler, airports: Dict[int, str],
         vmc_level_colors: Dict[int, str]):
    plotter.setup()
    while True:
        for index, icao in airports.items():
            try:
                metar = provider.fetch_metar_by_icao_code(icao)
                plotter.plot_airport(
                    Plot(
                        index,
                        vmc_level_colors[metar.vmc_level],
                        metar.text,
                    )
                )
            except (NoAvailableMetarDataException, NotAValidIcaoCodeException, NotAMetarException) as e:
                # skip airport if no data available, wrong ICAO or unable to decode
                print(str(e) + "... Skipping")
                plotter.plot_airport(
                    Plot(index, '#1E1E1E', icao)
                )
                continue
        throttler.wait()


main(
    provider=AvwxProvider(),
    plotter=NeoPixelPlotter(),
    throttler=ApiThrottler(
        daily_quota=settings.AVWX_WEATHER_API['daily_quota'],
        batch_size=len(settings.AIRPORTS)
    ),
    airports=settings.AIRPORTS,
    vmc_level_colors=settings.VMC_LEVEL_COLORS
)
