import unittest
import datetime

from pmm.plotter.daytimedetector import DaytimeDetector


class DaytimeDetectorTest(unittest.TestCase):
    def test_isDaytime(self):
        detector = DaytimeDetector('Paris')

        summer_datetime = datetime.datetime(2021, 6, 21, 19, 0, 0, tzinfo=datetime.timezone.utc)
        winter_datetime = datetime.datetime(2021, 12, 21, 19, 0, 0, tzinfo=datetime.timezone.utc)

        self.assertIs(detector.is_daytime(summer_datetime), True)
        self.assertIs(detector.is_daytime(winter_datetime), False)
