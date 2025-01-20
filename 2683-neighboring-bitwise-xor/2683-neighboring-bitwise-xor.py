class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        
        if n == 1:
            # Special case: only one element
            return derived[0] == 0

        # Try both possible starting points for original[0]
        for start in [0, 1]:
            current = start
            valid = True
            
            for i in range(n):
                # Compute the next element in original
                next_val = current ^ derived[i]
                current = next_val

                # For the last element, check cyclic consistency
                if i == n - 1 and current != start:
                    valid = False
            
            if valid:
                return True

        return False