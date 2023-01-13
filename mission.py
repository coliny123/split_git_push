import random

secret = random.randint(1, 10)
guess = int(input("1~10 사이의 숫자를 입력하시오: "))
if secret > guess:
    print(f"{secret} 보다 too low") # secret 확인 위해 fstring 사용
elif secret < guess:
    print(f"{secret} 보다 too high")
else:
    print(f"{secret} 과 just right")
