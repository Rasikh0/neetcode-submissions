class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1

        result = []
        total = 0

        for i in range(n):
            total += diff[i]
            shift = (ord(s[i]) - ord('a') + total) % 26
            result.append(chr(shift + ord('a')))

        return ''.join(result)
        