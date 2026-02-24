class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        last_pos = -1
        current_pos = 0
        
        while n > 0:
            # Check if the current bit is 1
            if n & 1:
                if last_pos != -1:
                    max_gap = max(max_gap, current_pos - last_pos)
                last_pos = current_pos
            
            # Shift right to check the next bit
            n >>= 1
            current_pos += 1
            
        return max_gap