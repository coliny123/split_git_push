#for문으로 10번 돌려서 랜덤은 1~200 초기값과 비교해서 큰수면 대체 작은수면 이긴 횟수 1
#이긴 횟수 출력과 마지막 수, 랜덤 값 10개 리스트
import random

list = list()
biggest = 0
win = 0
for i in range(1, 10):
    rand = random.randint(1, 200)
    list.append(rand)
    if biggest > rand:
        win = win+1
    else:
        biggest = rand
print(win, biggest, list)

