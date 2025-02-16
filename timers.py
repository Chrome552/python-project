# seconds
import time

def timer(t):
    t = int(t)
    i = 0
    while i<t:
        print(i)
        i += 1
        time.sleep(1)
    print("Time's up")

def cdt(t):
    t = int(t)
    while t>0:
        print(t)
        t -= 1
        time.sleep(1)
    print("Time's up")