import time
import random

class RandomTemp:
    def __init__(self, initial_temp):
        self.temp = initial_temp

    def get_a_new_temp(self):
        self.temp += random.random() - 0.5
        return self.temp

rt = RandomTemp(68)

temps = []
while True:
    time.sleep(1)
    temps.append(rt.get_a_new_temp())
    if len(temps) >= 3:
        avg_temp = (temps[-1] + temps[-2] + temps[-3]) / 3
        print(f"avg temp is {avg_temp}")
        if avg_temp < 67:
            print("ALERT TOO COLD!!!")
        if avg_temp > 70:
            print("ALERT TOO HOT!!!")
    else:
        print('waiting for more data...')
        print(f'initial guess is {sum(temps) / len(temps)}')


