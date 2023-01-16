#while

numbers = [1, 3, 5, 7]
position = 0
while position < len(numbers):
      number = numbers[position]
      if number % 2 == 0:
            print("짝수를 찾았습니다.",number)
            break
      position += 1
else:
      print("짝수가 없습니다.")

#
# while True:
#       dan = int(input("dan(0 to quit) : "))
#       if dan == 0:
#             break
#       elif 1< dan < 10:
#             i = 1
#             while i < 10:
#                   print("{0} * {1} = {2}".format(dan, i, dan * i))
#                   i = i + 1
#       else:
#             print("2에서 9사이의 값을 입력하세요.")