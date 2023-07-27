

# 14681 

# num_x = int(input())
# num_y = int(input())

# if num_x > 0:
#     if num_y > 0:
#         print(1)
#     else:
#         print(4)
# else:
#     if num_y > 0:
#         print(2)
#     else:
#         print(3)



# 2884

# hour, minute = input().split()

# my_hour = int(hour)
# my_minute = int(minute)


# if my_minute >= 45:
#     print(my_hour, my_minute - 45)
# else:
#     if my_hour == 0:
#         print(23, my_minute + 60 -45)
#     else:
#         print(my_hour - 1 , my_minute + 60 - 45)



# 2525

# hour, minute = input().split()

# my_time = int(input())

# my_hour = int(hour)
# my_minute = int(minute)

# result = my_time // 60
# remain = my_time % 60

# if  my_minute + remain >= 60:
#     if my_hour + result >= 23:
#         print(my_hour + result + 1 - 24, my_minute + remain - 60)
#     else:
#         print(my_hour + result + 1, my_minute + remain - 60)
# else:
#     if my_hour + result >= 24:
#         print(my_hour + result -24, my_minute + remain)
#     else:
#         print(my_hour + result, my_minute + remain)



# 2480

dice_a, dice_b, dice_c = map(int,input().split())

if dice_a == dice_b == dice_c:
    print(10000 + (dice_a * 1000))

elif dice_a != dice_b and dice_a != dice_c and dice_b != dice_c:
    dice_max = max(dice_a, dice_b , dice_c)
    print(dice_max * 100)

elif dice_a == dice_b != dice_c:
    print(1000 + (dice_a * 100))

elif dice_a == dice_c != dice_b:
    print(1000 + (dice_a * 100))

elif dice_b == dice_c != dice_a:
    print(1000 + (dice_b * 100))

else:
    pass