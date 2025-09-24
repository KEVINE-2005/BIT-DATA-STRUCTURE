from array import array
print('Project 72: Debate Tournament Scores ')
print('===Integers===')
marks = [60, 30, 40, 17, 98, 78]
total_marks = sum(marks)
avg = total_marks / len(marks)
max_marks = max(marks) 
print('Marks:', marks)
print("Total:", total_marks)
print("average:", avg)
print("minimum", min(marks))
print("Maximum", max_marks)

print('===Strings===')
print(f"Report for Debate Tournament Scores, totals = {sum(marks)}  and average = {sum(marks)/len(marks)}")

print('===Booleans===')
threshold = 50
print("if threshold >=50 and maximum marks > 80:")
if (threshold >= 50 and max_marks > 80):
    print('Above Standard')
else:
    print('Below Standard')

print('===Lists===')
ranks = [1,5,2,8,3,4,7,6]
print("ranks:", ranks)
ranks.append(9)
print("ranks after add elemnt", ranks)
ranks = [rank for rank in ranks if rank <= 3]

print("Ranks after condition, 3 first ranks will be rewarded:", ranks)
ranks.sort()
print("Ranks after sort:", ranks)

print("==== Arrays ====")

ranks_array = array('i', ranks)

print("ranks array:", ranks_array)
print("Sum of array compare to sum of list", sum(ranks_array) == ranks)

print("==== Dictionaries ====")

teams = [
    {"id": 1, "name": "Unstopable", "value": 13.5},
    {"id": 2, "name": "Smartworker", "value": 99.9},
    {"id": 3, "name": "Hardworker", "value": 12},
    {"id": 4, "name": "Winner", "value": 50},
    {"id": 5, "name": "Exceptional", "value": 100}
]
print("teams:", teams)

teams[4]['name'] = "fighter"
print("teams after update index 4", teams)
del teams[0]
print("teams after removeing index 0", teams)

total_values = sum([team['value'] for team in teams])

print("total of values of teams", total_values)

