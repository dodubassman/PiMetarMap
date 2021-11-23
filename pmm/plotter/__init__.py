from abc import ABC, abstractmethod
from collections.abc import Sequence
from dataclasses import dataclass


@dataclass
class Plot:
    index: int
    color: str
    icao: str


class PlotterInterface(ABC):

    @abstractmethod
    def setup(self, ) -> None:
        pass

    @abstractmethod
    def plot_airport(self, plot: Plot) -> None:
        pass

    @abstractmethod
    def plot_map(self, plots: Sequence[Plot]) -> None:
        pass
