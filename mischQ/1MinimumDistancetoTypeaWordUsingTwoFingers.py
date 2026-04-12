class Solution:
    def minimumDistance(self, word: str) -> int:
        memo = {}
        def get_dist(char1, char2):
            if char1 is None: return 0
            c1, c2 = ord(char1) - ord('A'), ord(char2) - ord('A')
            return abs(c1 // 6 - c2 // 6) + abs(c1 % 6 - c2 % 6)
        def solve(i, other_finger):
            if i == len(word):
                return 0
            state = (i, other_finger)
            if state in memo:
                return memo[state]
            target = word[i]
            prev = word[i-1] if i > 0 else None
            res1 = get_dist(prev, target) + solve(i + 1, other_finger)
            res2 = get_dist(other_finger, target) + solve(i + 1, prev)
            memo[state] = min(res1, res2)
            return memo[state]
        return solve(0, None)