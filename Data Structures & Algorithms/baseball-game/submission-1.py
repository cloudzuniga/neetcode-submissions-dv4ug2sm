class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for x in operations:
            match x:
                case '+':
                    scores.append(scores[-1] + scores[-2])
                case 'C':
                    scores.pop()
                case 'D':
                    scores.append(scores[-1] * 2)
                case _:
                    scores.append(int(x))
        return sum(scores)
        