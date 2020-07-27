# we are given an list [1, 2, 5]  sum = 5
# print all the changes which you can make by using the coins


def solve(a, sum, idx, res):
        if sum < 0:
                return
        if sum == 0:
                print(res)
                return

        if idx >= len(a):
                return

        res.append(a[idx])
        sum -= a[idx]
        solve(a, sum, idx, res)

        sum += a[idx]
        res.pop()
        solve(a, sum, idx + 1, res)

if __name__ == '__main__':
        solve([1,2,5], 10, 0, [])
