from abc import ABC, abstractmethod
from typing import Sequence
from dataclasses import dataclass


@dataclass
class Plot:
    index: int
    color: str
    text: str


class PlotterInterface(ABC):

    @abstractmethod
    def setup(self) -> None:
        pass

    @abstractmethod
    def plot_airport(self, plot: Plot) -> None:
        pass

    @abstractmethod
    def plot_map(self, plots: Sequence[Plot]) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def set_day_brightness(self) -> None:
        pass

    @abstractmethod
    def set_night_brightness(self) -> None:
        pass
