import random

#small = random.randint(0, 1)
#green = random.randint(0, 1)

#random.choice 사용
small = random.choice([True,False])
green = random.choice({True, False})
if small:
    if green:
        print("완두콩")
    else:
        print("체리")
else:
    if green:
        print("수박")
    else:
        print("호박")