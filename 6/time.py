import math

class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def add(self, B):
        result = Time(0, 0, 0)
        result.hour = self.hour + B.hour
        result.minute = self.minute + B.minute
        result.second = self.second + B.second
        return result

    def sub(self, B):
        result = Time(0, 0, 0)
        result.hour = self.hour - B.hour
        result.minute = self.minute - B.minute
        result.second = self.second - B.second
        return result

    def fix(self):
        if self.second >= 60:
            self.minute += math.floor(self.second / 60)
            self.second %= 60
        
        if self.minute >= 60:
            self.hour += math.floor(self.minute / 60)
            self.minute %= 60

        if self.second < 0:
            self.minute += math.floor(self.second / 60)
            self.second = 60 - ((self.second * -1) % 60)
        
        if self.minute < 0:
            self.hour += math.floor(self.minute / 60)
            self.minute = 60 - ((self.minute * -1) % 60)


    def timeToSec(self):
        seconds = (self.hour * 60 * 60) + (self.minute * 60) + (self.second)
        return seconds

    def secToTime(self, sec):
        time = {"hour": 0, "min": 0, "sec": 0}
        time["min"] = math.floor(sec / 60)
        time["sec"] = sec % 60

        if time["min"] > 59:
            time["hour"] = math.floor(time["min"] / 60)
            time["min"] %= 60
        
        return time

    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)

t1 = Time(4, -121, 30)
t2 = Time(3, 15, 12)

# t1.fix()
# t1.show()

time = t2.secToTime(3660)
print(time)


# t2.show()

# output = t1.add(t2)
# output.show()

# print("-------------")

# output = t1.sub(t2)
# output.show()
