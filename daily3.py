from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)

        answer = 0
        total = 0

        for i in range(n - 1, -1, -1):
            total += satisfaction[i]
            if total > 0:
                answer += total
            else:
                break
        return answer


# s = [-1,-8,0,5,-9]
# s = [4,3,2]
s = [-1,-4,-5]

print(Solution().maxSatisfaction(s))
