from typing import Tuple, Dict

from pmm import settings
from pmm.apithrottler import ApiThrottler
from pmm.metar.provider import ProviderInterface, NoAvailableMetarDataException
from pmm.metar.provider.avwxprovider import AvwxProvider
from pmm.plotter import PlotterInterface, Plot
from pmm.plotter.neopixelplotter import NeoPixelPlotter


def main(provider: ProviderInterface, plotter: PlotterInterface, throttler: ApiThrottler, airports: Tuple[str],
         vmc_level_colors: Dict[int, str]):
    plotter.setup()
    while True:
        for icao in airports:
            try:
                metar = provider.fetch_metar_by_icao_code(icao)
                plotter.plot_airport(
                    Plot(
                        airports.index(icao),
                        vmc_level_colors[metar.vmc_level],
                        icao,
                    )
                )
            except NoAvailableMetarDataException:
                # do nothing if no data available
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
