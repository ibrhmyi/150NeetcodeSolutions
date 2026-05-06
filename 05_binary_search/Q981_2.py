class TimeMap: #O(logk) time complexity with O(n) memory 

    def __init__(self):
        self.mydict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key] = []
        self.mydict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mydict:
            return ""

        pos = self.mydict[key]
        l, r = 0, len(pos) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            cur_timestamp = pos[m][1]

            if cur_timestamp == timestamp:
                return pos[m][0]
            elif cur_timestamp < timestamp:
                res = pos[m][0]
                l = m + 1
            else:
                r = m - 1

        return res


class TimeMap: #OPTIMIZED FASTER

    def __init__(self):
        self.dick = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dick[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dick or timestamp < self.dick[key][0][0]:
            return ""

        if timestamp >= self.dick[key][-1][0]:
            return self.dick[key][-1][1]

        pos = self.dick[key]
        l, r = 0, len(pos) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            if pos[m][0] <= timestamp:
                res = pos[m][1]
                l = m + 1
            else:
                r = m - 1

        return res
