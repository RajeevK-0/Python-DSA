class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Pre-defined primes up to 20 (since 2^20 > 10^6)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        
        for num in range(left, right + 1):
            # bin(num).count('1') is the simplest way to count set bits
            if bin(num).count('1') in primes:
                count += 1
                
        return count