# 1~49 六個號碼的亂數+一個特別號
#1.完成後使用git add 1.py
#2.使用git commit -m "完成大樂透號碼預測"
#3.改成函式
#4.一次產生5組
import random

def get_lotto(count):
    for i in range(count):
        lotto = []
        for i in range(count):
            lotto.append(random.randint(1, 49))
        lotto.sort()
        lotto.append(random.randint(1, 49))
        print(lotto)

get_lotto(5)