
def solveMinCoins(coinsArray, idx, sum):
    if sum == 0:
        return 0
    if sum < 0 or idx >= len(coinsArray):
        return 1000000000000000001

    if dp[idx][sum] != -1:
        return dp[idx][sum]
    
    ans =  min(
        1 + solveMinCoins(coinsArray, idx, sum - coinsArray[idx]), 
        solveMinCoins(coinsArray, idx + 1, sum)
        )
    dp[idx][sum] = ans
    return ans


if __name__ == '__main__':
    dp = [[-1 for x in range(1000)] for x in range(1000)]
    print(solveMinCoins([1,2,5], 0, 11))
   