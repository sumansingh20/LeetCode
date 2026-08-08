class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        right = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                right[j] = i
                j -= 1

            i -= 1

        ans = []

        j = 0
        used = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif used == False:
                if j == m - 1 or right[j + 1] > i:
                    ans.append(i)
                    j += 1
                    used = True

        if j == m:
            return ans

        return []