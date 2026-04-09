class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for x in operations:
            if x == '+':
                scores.append(scores[-1] + scores[-2])
            elif x == 'C':
                scores.pop()
            elif x == 'D':
                scores.append(scores[-1] * 2)
            else:
                scores.append(int(x))
        return sum(scores)
        