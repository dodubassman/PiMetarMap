import unittest

from pmm.metar.models import Metar


class MetarTest(unittest.TestCase):

    def test_vmc_level_computation(self):
        metar = Metar(
            'LFRS',
            'the complete metar string',
            2200,
            1400
        )
        self.assertEqual(metar.vmc_level, 1)

        metar = Metar(
            'LFRS',
            'the complete metar string',
            5000,
            9999
        )
        self.assertEqual(metar.vmc_level, 5)
