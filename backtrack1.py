def solve(a, idx, res):
        if idx == len(a):
                print(res)
                return
        res.append(a[idx])
        solve(a, idx + 1, res)

        res.pop()
        solve(a, idx + 1, res)

if __name__ == '__main__':
    solve([1,2,3], 0, [])


