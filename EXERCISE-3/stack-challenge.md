 # Challenge: Push ["X", "Y", "Z"], pop all, then push "W". Which is top?

 Step 1:
 define the stack
 stack = []
 Step 2 push element in stack
  stack.append("X")
  stack.append("Y")
  stack.append("Z")
Step 3: pop all
 we can use for loop or just pop step by step using step by step
 stack.pop()
 stack.pop()
 stack.pop()
now the stack is empty
Step 4: push(add new) "W"
stack.append("W")
print(stack)

the top of stack is "W"