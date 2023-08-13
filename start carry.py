#
#
# cases = int(input())
#
# ans= []
# for case in range(cases):
#     data = input()
#     acc = 0
#
#     for num in data.split(" "):
#         num = int(num)
#         isEven = num % 2 == 0
#         if(not isEven):
#             acc += num
#
#     ans.append(acc)
#
# for idx,val in enumerate(ans):
#     print("#{} {}".format(idx+1, val))


for row2 in range(4, 0, -1):
    print (row2)