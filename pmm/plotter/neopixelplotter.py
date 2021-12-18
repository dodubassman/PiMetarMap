import time
from typing import Sequence

import board
from neopixel import NeoPixel, RGB

from pmm import settings
from pmm.plotter import PlotterInterface, Plot
from pmm.plotter.daytimedetector import DaytimeDetector


class NeoPixelPlotter(PlotterInterface):
    """NeoPixel plotter, running on raspberrypi

       Handle plotting through WS2811/2812 addressable LED strip using NeoPixel library
    """

    pixels: NeoPixel
    daytime_detector: DaytimeDetector

    def setup(self) -> None:
        if settings.NEOPIXEL['gpio_pin'] == 'D10':
            pixel_pin = board.D10
        elif settings.NEOPIXEL['gpio_pin'] == 'D12':
            pixel_pin = board.D12
        elif settings.NEOPIXEL['gpio_pin'] == 'D18':
            pixel_pin = board.D18
        else:  # settings.NEOPIXEL['gpio_pin'] == 'D21':
            pixel_pin = board.D21

        num_pixels = settings.NEOPIXEL['num_pixels']
        self.pixels = NeoPixel(
            pixel_pin, num_pixels, pixel_order=RGB
        )
        self.pixels.fill((30, 30, 30))

        self.daytime_detector = DaytimeDetector(settings.CITY_LOCATION)

    def plot_airport(self, plot: Plot) -> None:

        localtime = time.localtime()
        if self.daytime_detector.is_daytime(localtime):
            self.set_day_brightness()
        else:
            self.set_night_brightness()

        hex_color = plot.color.lstrip('#')
        rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

        self.pixels[plot.index] = (rgb[0], rgb[1], rgb[2])

    def plot_map(self, plots: Sequence[Plot]) -> None:
        for plot in plots:
            self.plot_airport(plot)

    def clear(self):
        self.pixels.fill((0, 0, 0))

    def set_day_brightness(self):
        self.pixels.brightness = settings.NEOPIXEL['day_brightness']

    def set_night_brightness(self):
        self.pixels.brightness = settings.NEOPIXEL['night_brightness']
