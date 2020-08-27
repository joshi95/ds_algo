# problem 1 
# write an algorithm to find the fibonacci no

# memoization
class Fib:
    def __init__(self):
        self.dp = [-1] * (1000001)

    def fib_dp(self, no):
        if no < 0: 
            return 0
        if no == 1: return 0
        if no == 2: return 1
        if self.dp[no] != -1:
            return self.dp[no]
        self.dp[no] =  self.fib_dp(no - 1) + self.fib_dp(no - 2)
        return self.dp[no]

    def fib_recurssive(self, no):
        if no == 1: return 0
        if no == 2: return 1
        return self.fib_recurssive(no - 1) + self.fib_recurssive(no - 2) #O(2^n)

    def fib_tabular_dp(self, no):
        dp = [0] * (no + 1)
        dp[1] = 0
        dp[2] = 1
        for i in range(3, no + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[no]

if __name__ == '__main__':
    f = Fib()
    print(f.fib_tabular_dp(10))