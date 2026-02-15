class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Loop until both strings are exhausted and no carry remains
        while i >= 0 or j >= 0 or carry:
            # Get digits or 0 if pointer is out of bounds
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate sum and carry
            total = digit_a + digit_b + carry
            res.append(str(total % 2))
            carry = total // 2
            
            i -= 1
            j -= 1
            
        # Join list and reverse it to get final binary string
        return "".join(res[::-1])