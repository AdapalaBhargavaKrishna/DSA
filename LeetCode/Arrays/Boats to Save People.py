class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats

class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()

        left , right = 0, len(people) - 1
        boat = 0

        while left < right:
            if people[left] + people[right] > limit:
                right -= 1
                boat += 1
            
            else:
                boat += 1
                left += 1
                right -= 1

        if  left == right:
            boat += 1

        return boat