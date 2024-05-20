class Solution(object):
    def climbStairs(self, n):
        # Initialize an empty dictionary to store computed results
        memo = {}
        # Call the ways method with n and memo as arguments and return the result
        return self.ways(n, memo)
    
    def ways(self, n, memo):
        # Check if the result for n is already computed and stored in memo
        if n in memo:
            return memo[n]
        
        # Base cases: if n is 1 or 2, return 1 or 2 respectively
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        # Recursive case: calculate the result for n by summing up results for n-1 and n-2
        memo[n] = self.ways(n - 1, memo) + self.ways(n - 2, memo)
        # Store the calculated result in memo and return
        return memo[n]

# Example usage:
solution = Solution()
print(solution.climbStairs(5))  # Output: 8
