

# 수 이어가기

# N = int(input())
# my_list = [N]
# num = 0
# max_v = 0
# result = []
# for i in range(N+1):    # 자기 자신까지 검색 대상에 넣어야 반례 해결 가능( ex : 1 )
#     my_list.append(i)   # 두번째 숫자 넣고
#     while True:
#         num = my_list[-2] - my_list[-1]     # 끝에 두개끼리 뺀다.
#         if num >= 0:                        # 그 값이 0보다 크거나 같으면
#             my_list.append(num)             # 리스트에 추가
#         else:                               # 음수라면
#             break                           # while문 탈출
#
#     if max_v < len(my_list):                # 탈출 했을때 리스트 갯수 최댓값 구해 놓기
#         max_v = len(my_list)
#         result = my_list                    # 최댓값일때의 리스트 담아 놓기
#
#     my_list = [N]                           # 리스트 초기화
#
# print(max_v)
# print(*result)



# # 주사위 쌓기
#
# # 밑면 정하고 밑면 정하면 윗면 알수 있으니까
# # ex : 입력받은 배열 [0]-[5], [1]-[3], [2]-[4]
#
# import sys
# sys.stdin = open('wj.txt', 'r')
#
# N = int(input())
# for i in range(N):
#     dice = list(map(int, input().split()))
#     dice_top = 0
#     for j in range(6):
#






















