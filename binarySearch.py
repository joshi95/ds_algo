def binarySearchWithRecurssion(list, target, l, r):
    if l > r:
        return False
    mid = (l + r) // 2
    if list[mid] == target:
        return True
    
    if list[mid] > target:
        return binarySearchWithRecurssion(list, target, l, mid - 1)
    elif list[mid] < target:
        return binarySearchWithRecurssion(list, target, mid + 1, r)
    return False

if __name__ == '__main__':
    l  = [1,2,3,4,5]
    print(binarySearchWithRecurssion(l, 33, 0, len(l) - 1))
    