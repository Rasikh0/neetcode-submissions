class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # Part 1: split the flowers into two sorted lists
        starts = []
        ends = []
        for start, end in flowers:
            starts.append(start)
            ends.append(end)
        starts.sort()
        ends.sort()

        # Part 2: answer each person with the party trick
        answer = []
        for t in people:
            started = self.count_at_most(starts, t)
            ended = self.count_at_most(ends, t - 1)
            answer.append(started - ended)
        return answer

    # Part 3: how many numbers in a sorted list are at most t
    def count_at_most(self, nums: List[int], t: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= t:
                low = mid + 1
            else:
                high = mid - 1
        return low