dp = [[[None for x in range(100)] for x in range(100)] for x in range(100)]

def solve(A, start, end, year):
    global dp
    if start > end:
        return 0

    if dp[start][end][year] != None:
        return dp[start][end][year]

    ans =  max(
        (A[start] * year) + solve(A, start + 1, end, year + 1),
        (A[end] * year) + solve(A, start, end - 1, year + 1)
    )
    dp[start][end][year] = ans
    return ans

# 3 dimention array to store the states


A = [2,4,6,2,5]

if __name__ == '__main__':
    print(solve(A, 0, len(A) - 1, 1))
    


