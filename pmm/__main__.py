from pmm import settings
from pmm.metar.provider.inmemoryprovider import InMemoryProvider as Provider
from pmm.plotter import Plot
from pmm.plotter.cliplotter import CliPlotter

provider = Provider()
plots = []
for icao in settings.AIRPORTS:
    metar = provider.fetch_metar_by_icao_code(icao)
    plots.append(
        Plot(
            settings.AIRPORTS.index(icao),
            settings.VMC_LEVEL_COLORS[metar.vmc_level],
            icao,
        )
    )

plotter = CliPlotter()
plotter.setup()
plotter.plot_map(plots)
