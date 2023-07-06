import random

print("로또 번호 다섯개를 추첨하자!")

for i in range(5):
    lotto = random.sample(range(1,46),6)
    print(lotto)
