class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque()
        visited = set()
        queue.append(start)
        while queue:
            temp = queue.popleft()
            if arr[temp] == 0:
                return True
            for i in (temp+arr[temp],temp-arr[temp]):
                if 0<= i < len(arr) and i not in visited:
                    visited.add(i)
                    queue.append(i)
            
        return False