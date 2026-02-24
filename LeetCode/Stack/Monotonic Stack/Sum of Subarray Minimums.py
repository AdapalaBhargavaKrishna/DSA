class Solution(object):
    def sumSubarrayMins(self, arr):
        n = len(arr)
        MOD = 10**9 + 7
        stack = []
        left = [-1] * n
        right = [n] * n

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0

        for i in range(n):
            ans += arr[i] * (i - left[i]) * (right[i] - i)

        return ans % MOD