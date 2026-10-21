class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        is_sorted = True
        for i in range(n - 1):
            if s[i] > s[i + 1]:
                is_sorted = False
                break
        if is_sorted:
            return 0
        if n == 2:
            return -1
        min_char = min(s)
        max_char = max(s)
        if s[0] == min_char or s[n - 1] == max_char:
            return 1
        first_is_unique_max = True
        for i in range(1, n):
            if s[i] >= s[0]:
                first_is_unique_max = False
                break
        last_is_unique_min = True
        for i in range(n - 1):
            if s[i] <= s[n - 1]:
                last_is_unique_min = False
                break
        if first_is_unique_max and last_is_unique_min:
            return 3
        return 2