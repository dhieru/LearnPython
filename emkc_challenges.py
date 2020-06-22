# Reverse a string
value1 = 'cat'
print(value1[::-1])

# Count of elements which appears the most in a string
val2 = {x:value1.count(x) for x in value1}
for k,v in val2.items():
        if v == max(val2.values()):
                     return k

# Take a string of comma separated numbers and print out the sum
value1 = '1,2,3,4,5'
val2 = {x:value1.count(x) for x in value1}
for k,v in val2.items():
    if v == max(val2.values()):
        return k

# Count of elements which appears the most in a string
val2 = {x:value1.count(x) for x in value1}
for k,v in val2.items():
    if v == max(val2.values()):
         return k

# Take a string of comma separated numbers and print out the sum
value1 = '1,2,3,4,5'
val2 = {x:value1.count(x) for x in value1}
for k,v in val2.items():
    if v == max(val2.values()):
         return k

# Integer list sorting
import sys

value1 = sys.argv[1]

# write your solution here
val2  = value1.split(',')
val3 = [ int(x.strip()) for x in val2]

val5 = sorted(val3, reverse=True)
#print(str(val5).strip('[]'))
print(','.join(map(str,val5)))

val1 = 'run,barn,yellow,barracuda,shark,fish,swim'
# Find longest word
import sys

value1 = sys.argv[1]

# write your solution here
val1 = value1.split(',')
val2 = {x:len(x) for x in val1}
result = []
for k,v in val2.items():
    if v == max(val2.values()):
        result.append(k.lower())
print(','.join(result))