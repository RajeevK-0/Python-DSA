class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        required_count = 1 << k
    
        # A set to store unique substrings of length k
        seen = set()
        
        # Iterate through the string to extract all substrings of length k
        for i in range(len(s) - k + 1):
            substring = s[i : i + k]
            seen.add(substring)
            
            # Optimization: If we've found all codes, we can stop early
            if len(seen) == required_count:
                return True
                
        return False