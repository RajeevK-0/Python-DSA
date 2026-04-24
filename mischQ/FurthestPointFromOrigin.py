class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        countL = 0
        countR = 0
        count_ = 0
        for char in moves:
            if char == 'L':
                countL += 1
            elif char == 'R':
                countR += 1
            else:
                count_ += 1
        # Calculate the net distance and add the wildcards
        return abs(countL - countR) + count_