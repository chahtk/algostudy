result = []

def solve(line):
  stack = []

  for i in range(len(line)):
    char = line[i]
    if char == '(':
      stack.append('s')
    elif char == '[':
      stack.append('b')
    elif char == ')':
      if len(stack) > 0:
        if stack[len(stack) - 1] == 's':
          stack.pop()
        else:
          return 'no'
      else:
        return 'no'
    elif char == ']':
      if len(stack) > 0:
        if stack[len(stack) - 1] == 'b':
          stack.pop()
        else:
          return 'no'
      else:
        return 'no'
  if len(stack) == 0:
    return 'yes'
  return 'no'

while True:
  line = input()
  if line == '.':
    break
  result.append(solve(line))

for item in result:
  print(item)