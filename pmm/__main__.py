from typing import Dict
import datetime
import time

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

    night_start_time = datetime.time(settings.NIGHT_HOURS[0])
    night_end_time = datetime.time(settings.NIGHT_HOURS[1])

    while True:
        now_time = datetime.datetime.now().time()
        # Don't run at night
        if night_end_time <= now_time < night_start_time:
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
                        Plot(index, '#282828', icao)
                    )
                    continue
                except Exception as e:
                    # Turn off LEDs and raise error if uncatched
                    plotter.clear()
                    raise e

            throttler.wait()
        else:
            # Switch of lights at night
            plotter.clear()
            time.sleep(60)


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
