"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)

        rooms = []

        for interval in intervals:
            start, end = interval.start, interval.end
            if rooms and start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)

        return len(rooms)