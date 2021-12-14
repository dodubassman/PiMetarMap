import time
from typing import Sequence

import board
from neopixel import NeoPixel, RGB

from pmm.plotter import PlotterInterface, Plot
from pmm import settings


class NeoPixelPlotter(PlotterInterface):
    """NeoPixel plotter, running on raspberrypi

       Handle plotting through WS2811/2812 addressable LED strip using NeoPixel library
    """

    pixels: NeoPixel

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

    def plot_airport(self, plot: Plot) -> None:

        localtime = time.localtime()
        if localtime.tm_hour < 6 or localtime.tm_hour > 18:
            self.set_night_brightness()
        else:
            self.set_day_brightness()

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
