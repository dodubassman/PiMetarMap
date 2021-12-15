import math
import threading
from dataclasses import dataclass
import time


@dataclass
class ApiThrottler:
    """
    Api throttler waits for the good number of seconds between the next batch of api endpoint calls

    In order not to burst the max Api quotas, calls have to be limited within the next 24hours.
    The throttler compute the number of second you have to pause your requests before the next call.

    Attributes
    ----------
    self.daily_quota : int
        Number of calls allowed by the api during a 24h range.
    self.is_nightly_run : bool
        Do the api has to be called during the 2am - 6am hour range. Allow you to save some calls. Default is true
    self.batch_size : int
        Number of calls you have to do in a one "batch" of request. Some usages could require a minimum number of calls
        for each application cycle. Default is 1.
    """
    daily_quota: int
    is_nightly_run: bool = True
    batch_size: int = 1

    def wait(self) -> None:
        calls_per_hour = self.daily_quota / self.batch_size / 24
        delay_between_calls = math.ceil(3600 / calls_per_hour)
        print("Waiting " + str(delay_between_calls) + "s.")
        time.sleep(delay_between_calls)
