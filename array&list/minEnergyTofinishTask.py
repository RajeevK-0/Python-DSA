class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort by the difference between minimum and actual (descending)
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        initial_energy = 0
        current_energy = 0
        
        for actual, minimum in tasks:
            if current_energy < minimum:
                # We need to increase our starting pool to meet the requirement
                shortfall = minimum - current_energy
                initial_energy += shortfall
                current_energy += shortfall
            
            # Spend the energy
            current_energy -= actual
            
        return initial_energy
        
        