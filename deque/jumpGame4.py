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
        