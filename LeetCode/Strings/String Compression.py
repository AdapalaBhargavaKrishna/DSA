class Solution(object):
    def compress(self, chars):
        write = 0
        left = 0

        for right in range(len(chars) + 1):
            if right == len(chars) or chars[right] != chars[left]:
                chars[write] = chars[left]
                write += 1

                count = right - left
                if count > 1:
                    for c in str(count):
                        chars[write] = c
                        write += 1
                
                left = right
        return write

# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# Example 2:
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.