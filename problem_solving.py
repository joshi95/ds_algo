# left = 0
# right = len(a) - 1

# while left <= right:
#     ans = a[left] + a[right]
#     if ans == k:
#         return True
#     elif ans > k:
#         right -= 1
#     elif ans < k:
#         left += 1

# return False

[False, True, False, False, False]


m = [False] * (1000)
a =  [1,2,34,55,4,2]
k = 89
for i in enumerate(a):
    if m[k - i]:
        print("found the two elements", i, k-i)
    m[i] = True

# if in the list the particular index is true
# that means that particular index value we have
# visited already.