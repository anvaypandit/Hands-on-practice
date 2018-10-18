#Definition for an interval.

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


Interval1 = Interval(8,10)
Interval2 = Interval(15,18)
Interval3 = Interval(2,6)
Interval4 = Interval(1,3)
intervals = [Interval1,Interval2,Interval3,Interval4]

# sort these intervals based on start time
intervals.sort(key=lambda x: x.start)

merged = []
for interval in intervals:
    if not merged or merged[-1].end < interval.start:
        merged.append(interval)
    else:
        merged[-1].end = max(merged[-1].end,interval.start)



        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged

