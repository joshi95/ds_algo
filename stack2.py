# buildings = [2, 4, 8]

def solve(buildings):
    ans = 0
    for i in range(0, len(buildings)):
        
        right_blocking_building_idx = -1
        left_blocking_building_idx = -1

        for right in range(i + 1, len(buildings)):
            if buildings[right] > buildings[i]:
                right_blocking_building_idx = right
                break

        for left in range(i - 1, -1, -1):
            if buildings[left] > buildings[i]:
                left_blocking_building_idx = left
                break
        
        if left_blocking_building_idx == -1 or right_blocking_building_idx == -1:
            ans += 0   
        else:
            ht = min(buildings[right_blocking_building_idx], buildings[left_blocking_building_idx]) - buildings[i]
            breath = abs(right_blocking_building_idx - left_blocking_building_idx) - 1
            ans += ht * breath
    return ans

if __name__ == '__main__':
    print(solve([4, 2, 8]))
    