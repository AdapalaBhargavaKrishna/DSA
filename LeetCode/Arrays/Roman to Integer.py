class Solution(object):
    def romanToInt(self, s):
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result = 0
        prev_value = 0

        for i in reversed(s):
            curr_value = roman[i]
            if curr_value < prev_value:
                result -= curr_value
            else:
                result += curr_value
            prev_value = curr_value          
        return result
    
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.