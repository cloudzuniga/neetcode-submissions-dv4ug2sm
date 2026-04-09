class Solution:
    def isValid(self, s: str) -> bool:
        brackets = list(s)
        ops = []
        if len(brackets) <=1 or brackets[0] in '}])':
            return False
        else:
            for x in brackets:
                if x in '{[(':
                    ops.append(x)
                else:
                    if len(ops)>0 and (ord(ops[-1])//10 == ord(x)//10):
                        ops.pop()
                    else:
                        ops.append(x)
                        break
        print(ops)
        return False if len(ops)>0 else True

        