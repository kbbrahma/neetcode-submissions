class Solution:
  def isValid(self, s: str) -> bool:
    pmap = {')':'(', ']':'[', '}':'{'}
    stack = []
    for p in s:
      if p not in pmap.keys():
        stack.append(p)
      else:
        if len(stack) and pmap.get(p) == stack[-1]:
          stack.pop()
        else:
          return False
    if len(stack):
      return False
    else:
      return True       

        