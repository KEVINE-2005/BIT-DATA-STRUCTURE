from collections import deque
print("Stack Questions: \n Practical (Rwanda): UR pushes ")
ur = []
ur.append("Lab1")
ur.append("Lab2")
ur.append("Lab3")
print("Ur pushes:",ur)
ur.pop()
print("Ur pushes after pop:",ur)
print('Ur push top is equal to: ', 'none' if len(ur)== 0 else ur[-1])


print("Irembo Stack Questions:")
irembo = []
irembo.append("Step1")
irembo.append("Step2")
irembo.append("Step3")
print("Irembo pushes:",irembo)
irembo.pop()
print("irembo pushes after undo one:",irembo)
print('Left step in irembo: ', irembo)


# codes for challenge

 #Step 1:
 #define the stack
stack = []
 #Step 2 push element in stack
stack.append("X")
stack.append("Y")
stack.append("Z")
#Step 3: pop all
 #we can use for loop or just pop step by step using step by step
stack.pop()
stack.pop()
stack.pop()
#now the stack is empty
#Step 4: push(add new) "W"
stack.append("W")
print(stack)

#the top of stack is "W"

print("Reflection: Why stack represents temporary memory?")
print("Becouse the the code in stack will be excuted at runtime, after the memory will be cleaned.")

print("Queue Questions:")
print("Practical RRA:")
rra = deque()
rra.append("citizen 1")
rra.append("citizen 2")
rra.append("citizen 3")
rra.append("citizen 4")
rra.append("citizen 5")
rra.append("citizen 6")

print('RRA queue', rra)
print('RRA 0 index was served', rra.popleft())
print('RRA 1 index was served', rra.popleft())
print("Front is ", rra[0])

print("At BK ATM, 10 clients queue. Who is last?")
bk_atm = deque()
bk_atm.append("client 1")
bk_atm.append("client 2")
bk_atm.append("client 3")
bk_atm.append("client 4")
bk_atm.append("client 5")
bk_atm.append("client 5")
bk_atm.append("client 7")
bk_atm.append("client 8")
bk_atm.append("client 9")
bk_atm.append("client 10")
print("Last client is:", bk_atm[-1])

print("Challenge: Queue vs stack for event entry. Which works?")
print("Challenge: Queue vs stack for event entry. Which works?")
print("Answer: Queue becouse who booked first will be served first")
print("Reflection: Why FIFO ensures fairness in public events?")
print("Answer becouse FIFO is first in first out principal the fisrt person to book ticket will be served first and get the ticket first, but the last one can be served last which ensure fairness")



