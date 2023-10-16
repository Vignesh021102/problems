def check(string):
  stack = []
  ColseChar = "]})"
  for char in string:
    print(char,"  ",stack)
    if char in ColseChar:
      #see the stack
      try:
        match(char):
          case "]":
            if stack[-1] != "[":
              return False
            stack.pop()         
          case "}":
            if stack[-1] != "{":
              return False
            stack.pop()
          case ")":
            if stack[-1] != "(":
              return False
            stack.pop()
      except:
        return False
    else:
      stack.append(char)
  if len(stack) == 0:
    return True
  return False
print(check("[()]"))
print(check("[()}]"))
print(check("[({)}]"))