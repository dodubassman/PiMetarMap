from typing import Sequence

from pmm.plotter import PlotterInterface, Plot


class CliPlotter(PlotterInterface):
    """A Cli plotter, mainly used for functional tests

       Displays in your terminal the airport list with colored plots matching VMC conditions
       Exemple :
           ⬤ LFRS 231800Z AUTO 05012KT CAVOK 07/M02 Q1023 TEMPO 05015G25KT
    """

    def setup(self) -> None:
        print('Metar map preview')

    def plot_airport(self, plot: Plot) -> None:
        hexcolor = plot.color.lstrip('#')

        rgb = tuple(int(hexcolor[i:i + 2], 16) for i in (0, 2, 4))

        print(f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{'⬤'}\033[m", end='  ')
        print(plot.text)

    def plot_map(self, plots: Sequence[Plot]) -> None:
        for plot in plots:
            self.plot_airport(plot)

    def clear(self) -> None:
        pass

    def set_day_brightness(self) -> None:
        pass

    def set_night_brightness(self) -> None:
        pass
