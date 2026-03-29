class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (sorted([s1[0],s1[2]]) == sorted([s2[0], s2[2]]) and
                sorted([s1[1],s1[3]]) == sorted([s2[1], s2[3]]))
####################################################################
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        even_s1 = sorted([s1[0], s1[2]])
        even_s2 = sorted([s2[0], s2[2]])
        
        odd_s1 = sorted([s1[1], s1[3]])
        odd_s2 = sorted([s2[1], s2[3]])
        
        return even_s1 == even_s2 and odd_s1 == odd_s2
#####################################################################
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Check even positions (0 and 2)
        # We check if the sorted pair from s1 matches the sorted pair from s2
        even_match = sorted([s1[0], s1[2]]) == sorted([s2[0], s2[2]])
        
        # Check odd positions (1 and 3)
        odd_match = sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]])
        
        return even_match and odd_match
#######################################################################
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1_list = list(s1)
        s2_list = list(s2)

        i = 0
       
        while i < 2:
            j = i + 2
            if s1[i] != s2[i] and s1[j] != s2[j]:
                s1_list[i], s1_list[j] = s1_list[j], s1_list[i] 
            print("s1_list:", s1_list)
            if s1_list == s2_list:
                return True
            i += 1
            
        return False