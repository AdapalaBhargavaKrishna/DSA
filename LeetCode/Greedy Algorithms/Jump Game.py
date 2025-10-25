def canJump(nums):
    maxReach = 0

    for i, num in enumerate(nums):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + num)
    return True

print(canJump([2,3,1,1,4]))  # True
print(canJump([3,2,1,0,4]))  # False
print(canJump([0]))          # True
print(canJump([2,0,0]))      # True