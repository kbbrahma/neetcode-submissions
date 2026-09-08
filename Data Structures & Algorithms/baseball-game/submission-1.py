class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for op in operations:
            match(op):
                case "+":
                    ans.append(ans[-1]+ans[-2])
                case "D":
                    ans.append(ans[-1]*2)
                case "C":
                    ans.pop()
                case _:
                    ans.append(int(op))
        return sum(ans)            


     