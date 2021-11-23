import unittest

from pmm.plotter.cliplotter import CliPlotter
from pmm.plotter import Plot
from pmm import settings


class CliPlotterTest(unittest.TestCase):
    def test_plot_airport(self):
        plotter = CliPlotter()
        plotter.setup()

        plots = (
            Plot(0, settings.VMC_LEVEL_COLORS[5], 'LFRS'),
            Plot(0, settings.VMC_LEVEL_COLORS[4], 'LFJB'),
            Plot(0, settings.VMC_LEVEL_COLORS[3], 'LFOU'),
            Plot(0, settings.VMC_LEVEL_COLORS[2], 'LFRN'),
            Plot(0, settings.VMC_LEVEL_COLORS[1], 'LFII')
        )

        plotter.plot_map(plots)
