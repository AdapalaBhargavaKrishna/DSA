# Insert Delete GetRandom O(1)

import random
class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.index_map = {}

    def insert(self, val):
        if val in self.index_map:
            return False
        self.index_map[val] = len(self.nums)
        self.nums.append(val)
        return True
        

    def remove(self, val):
        if val not in self.index_map:
            return False

        last_element = self.nums[-1]
        index_replace = self.index_map[val]

        self.nums[index_replace] = last_element
        self.index_map[last_element] = index_replace

        self.nums.pop()
        del self.index_map[val]
        return True

    def getRandom(self):
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



# Input:
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output:
# [null, true, false, true, 2, true, false, 2]
# Explanation:
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.