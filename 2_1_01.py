class Clock:
    def __init__(self):
        self.__time = 0

    def __check_time(self, tm):
        return type(tm) is int and 0 <= tm < 10_000

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time


clock = Clock()
clock.set_time(4530)
print(clock.get_time())
