# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         i = 0 
#         j = len(s)-1
#         while i<j:
#             if not s[i].isalnum():
#                 i+=1
#             elif not s[j].isalnum():
#                 j-=1
#             else:
#                 if s[i].lower()!=s[j].lower():
#                     return False
#                 i+=1
#                 j-=1
#         return True
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         i = 0 
#         j = len(s)-1
#         while i<j:
#             while i<j and not s[i].isalnum():
#                 i+=1
#             while i<j and not s[j].isalnum():
#                 j-=1
#             if s[i].lower()!=s[j].lower():
#                 return False
#             i+=1
#             j-=1
#         return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(c for c in s if c.isalnum())
        t = t.lower()
        i = 0
        j = len(t)-1
        while i<=j:
            if t[i] != t[j]:
                return False 
            i+=1
            j-=1
        return True