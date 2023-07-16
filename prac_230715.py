

# case = input()
# case = case.split()
# print (int(case[0]) + int(case[1]))





# case = int(input())
# print(case - 543)





case = input()
case = case.split()

A = int(case[0])
B = int(case[1])
C = int(case[2])

print ((A+B) % C)
print (((A%C) + (B%C))%C)
print ((A*B) % C)
print (((A%C) * (B%C))%C)