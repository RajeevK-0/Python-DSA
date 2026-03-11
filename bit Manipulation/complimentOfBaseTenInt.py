class Solution:
    def bitwiseComplement(self, n: int) -> int:
        t = bin(n)
        res = ''
        print(t)
        j = 0
        while j < len(t):
            if j != 1:
                j+=1
            else:    
                for i in range(j,len(t)):
                    if t[i] == "0":
                        res+="1"
                    else:
                        res+="0"
                break
        return int(res,2)