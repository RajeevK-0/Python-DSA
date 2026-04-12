class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Create a list of robots with their original index to preserve output order
        n = len(positions)
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
        
        # Sort robots by position
        robots.sort()
        
        stack = []  # Will store robots moving Right 'R'
        
        for i in range(len(robots)):
            curr = robots[i]
            
            # If moving Right, it won't collide with anything to its left
            if curr[2] == 'R':
                stack.append(curr)
                continue
            
            # If moving Left, check for collisions with robots moving Right in the stack
            while stack and curr[1] > 0 and stack[-1][2] == 'R':
                top = stack[-1]
                
                if curr[1] > top[1]:
                    # Left robot wins
                    stack.pop()
                    curr[1] -= 1
                elif curr[1] < top[1]:
                    # Right robot wins
                    top[1] -= 1
                    curr[1] = 0 # Left robot destroyed
                else:
                    # Both destroyed
                    stack.pop()
                    curr[1] = 0
            
            # If Left robot survived all collisions, add it to stack/result
            if curr[1] > 0:
                stack.append(curr)
                
        # Sort by original index and return healths
        stack.sort(key=lambda x: x[3])
        return [r[1] for r in stack]