class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        if n == 1:
            return 0
            
        # Track visited nodes to avoid redundant processing
        visited = [False] * n
        
        # Group indices by their array values
        mp = defaultdict(list)
        for i, val in enumerate(arr):
            mp[val].append(i)
            
        # Initialize BFS queue with the starting index (0)
        que = deque([0])
        visited[0] = True
        
        steps = 0
        
        while que:
            size = len(que)
            
            # Process all elements at the current BFS level
            for _ in range(size):
                curr = que.popleft()
                
                # Destination reached
                if curr == n - 1:
                    return steps
                    
                # Option 1: Move left
                left = curr - 1
                if left >= 0 and not visited[left]:
                    que.append(left)
                    visited[left] = True
                    
                # Option 2: Move right
                right = curr + 1
                if right < n and not visited[right]:
                    que.append(right)
                    visited[right] = True
                    
                # Option 3: Jump to identical values
                if arr[curr] in mp:
                    for idx in mp[arr[curr]]:
                        if not visited[idx]:
                            que.append(idx)
                            visited[idx] = True
                    
                    # Erase the entry to avoid TLE on future duplicate lookups
                    del mp[arr[curr]]
            
            steps += 1
            
        return -1
        # mp = {}
        # for i in range(len(arr)):
        #     if arr[i] in mp:
        #         mp[arr[i]].append(i)
        #     else:
        #         mp[arr[i]] = [i]
        # visited = set()
        # queue = deque()
        # queue.append(0)
        # i = 0
        # ans = 0
        # while queue:
        #     t = queue.popleft()
        #     visited.add(t)
        #     if i == len(arr)-1:
        #         return ans
        #     if mp[arr[t]][-1] != t:
        #         i = mp[arr[t]][-1]
        #         visited.add(i)
        #         queue.append(mp[arr[t]][-1])
        #         ans += 1
        #     else:
        #         for j in (t-1 , t+1):
        #             if (0<= j < len(arr) and j+2 > len(arr)-1 ) or (0<= j < len(arr) and j-2 <0) or (0<= j < len(arr) and mp[arr[j]][-1] > mp[arr[j+2]][-1] )or (0<= j < len(arr) and mp[arr[j]][-1] > mp[arr[j-2]][-1] ) :
        #                 i = j
        #                 visited.add(j)
        #                 queue.append(j)
        #                 ans+=1


        # while i < len(arr):
        #     if i == len(arr)-1:
        #         return ans
        #     t = queue.popleft()
        #     pos = mp[arr[t]][-1]
        #     if pos != t : 
        #         queue.append(arr[pos])
        #         i = pos
        #         ans+=1
        #     elif pos == t and t !=0:
        #         for j in (t-1,t+1):
        #             if mp[arr[j]][-1] >= mp[arr[j+2][-1]] or mp[arr[j]][-1] >= mp[arr[j-2][-1]]  :
        #                 visited.add(arr[j])
        #                 queue.append(j)
        #                 i = j
        #                 ans+=1
        #     else:
        #         visited.add(arr[t+1])
        #         queue.append(t+1)
        #         i = t+1
        #         ans+=1

