class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []
        
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                # We found an atomic special string s[i:j+1]
                # 1. Strip the first '1' and last '0' -> s[i+1:j]
                # 2. Recursively solve for the inner part
                # 3. Add '1' + result + '0' to our list
                res.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
                i = j + 1
                
        # Sort the special strings in descending order to get the lexicographically largest
        return "".join(sorted(res, reverse=True))