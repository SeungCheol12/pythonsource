# 모듈
# 함수, 변수 클래스를 모아 놓은 파이썬 파일

# import math
# import sys

# print(math.sqrt(25))
# print(math.sin(2))
# print(sys.builtin_module_names)

# math 모듈에서 사용할 함수만 가져오기
# from math import sin, cos, floor, ceil

# print(sin(60))
# print(cos(1))
# print(floor(1.5))
# print(ceil(1.6))

# from random import random, uniform, randrange, choice, shuffle, sample

# print(random())  # 0 < random() <= 1
# print(uniform(10, 20))  # 10 ~ 20 사이를 float 로 리턴
# print(randrange(10, 20))  # 10 ~ 20 사이를 int 로 리턴
# print(choice([1, 2, 3, 4, 5, 6, 7, 8, 10, 20]))  # 주어진 list 안에서 랜덤하게 선택
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 20]
# shuffle(list1)  # 섞기
# print(list1)  # 섞은 후 결과 확인
# print(sample(list1, 2))  # 원하는 요소 개수만큼 추출

# import math as m

# print(m.ceil(3.14))
# print(m.sin(3))

# 커스텀 모듈 호출
# import prt

# prt.prt1()
# prt.prt2()

# import sum1

# print(sum1.add(6, 7))

# number1 = sum1.number_input()
# print("둘레", sum1.get_circ(number1))
# print("면적", sum1.get_area(number1))

from calc import Calc

calc = Calc(6, 5)
print(calc.add())
print(calc.mul())
