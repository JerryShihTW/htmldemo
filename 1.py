# 1~49 六個號碼的亂數+一個特別號
#1.完成後使用git add 1.py
#2.使用git commit -m "完成大樂透號碼預測"
#3.改成函式
#4.一次產生5組
import random
lotto = []
for i in range(6):
    lotto.append(random.randint(1, 49))
lotto.sort()
lotto.append(random.randint(1, 49))
print(lotto)