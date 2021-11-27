import unittest
import time

from pmm.apithrottler import ApiThrottler


class ApiThrottlerTest(unittest.TestCase):
    def test_throttling_waiting_time(self):
        apithrottler = ApiThrottler(
            daily_quota=24 * 1800,  # 1 call every 2 secondes
        )
        start_time = time.localtime()
        apithrottler.wait()
        end_time = time.localtime()

        self.assertEqual(end_time.tm_sec - start_time.tm_sec, 2)
