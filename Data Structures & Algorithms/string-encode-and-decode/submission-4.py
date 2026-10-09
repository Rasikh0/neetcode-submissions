class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        n = len(s)

        while i < n:
            j = s.index('#', i)
            length = int(s[i:j])
            j += 1
            res.append(s[j:j+length])
            i = j + length
        return res