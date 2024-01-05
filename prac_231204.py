

import random

ans = [1, 27, 7, 14, 12, 8]
li = [i+1 for i in range(27)]
box = []
res = 0

print('뽑은 숫자 : ', end='')
for k in range(6):
    num = random.choice(li)
    li.remove(num)
    box.append(num)
    print(num, end=' ')
print()

for b in box:
    if b in ans:
        res += 1

if res == 3:
    print('4등 당첨입니다. (5000원 당첨)')
elif res == 4:
    print('3등 당첨입니다. (100만원 당첨)')
elif res == 5:
    print('2등 당첨입니다. (5000만원 당첨)')
elif res == 6:
    print('1등 당첨입니다. (10억 당첨)')
else:
    print('꽝입니다. 1000원 날리셨네요 ㅎㅎ')

