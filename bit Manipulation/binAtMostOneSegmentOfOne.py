import numpy as np
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # Convert string to a NumPy array of integers
        arr = np.array(list(s), dtype=int)
        
        # Calculate the difference between adjacent elements: arr[i+1] - arr[i]
        diff = np.diff(arr)
        
        # A "01" pattern results in a +1 in the diff array
        # If any element in diff is 1, there's a second segment
        return not np.any(diff == 1)