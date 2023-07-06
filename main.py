
import random

print("로또 번호 다섯개!")

import readom

print(" 로또 번호 다섯개를 추첨하자!")


for i in range(5):
    lotto = random.sample(range(1,46),6)
    print(lotto)

y = input("다시 추첨하기 원하면 y를 누르세요:")

if y == "y" :
    lotto =  random.sample(range(1,46),6)
    print(lotto)

