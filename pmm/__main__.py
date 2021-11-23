from typing import Tuple, Dict

from pmm import settings
from pmm.metar.provider import ProviderInterface
from pmm.metar.provider.inmemoryprovider import InMemoryProvider as Provider
from pmm.plotter import PlotterInterface, Plot
from pmm.plotter.cliplotter import CliPlotter


def main(provider: ProviderInterface, plotter: PlotterInterface, airports: Tuple[str],
         vmc_level_colors: Dict[int, str]):
    plots = []
    for icao in airports:
        metar = provider.fetch_metar_by_icao_code(icao)
        plots.append(
            Plot(
                airports.index(icao),
                vmc_level_colors[metar.vmc_level],
                icao,
            )
        )

    plotter.setup()
    plotter.plot_map(plots)


if __name__ == "__main__":
    main(
        provider=Provider(),
        plotter=CliPlotter(),
        airports=settings.AIRPORTS,
        vmc_level_colors=settings.VMC_LEVEL_COLORS
    ),
