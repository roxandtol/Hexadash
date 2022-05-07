import time


class StopWatch():
    def __init__(self) -> None:
       self.reset()

    def reset(self):
        self.startTime = 0

    def start(self):
        self.startTime = time.time()

    def currentTime(self) -> float:
        if self.startTime == 0:
            return 0
        return time.time() - self.startTime