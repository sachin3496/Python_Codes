import time
from threading import Thread

answer = None

def check():
    time.sleep(3)
    if answer != None :
        return 
    print("Too Slow")

t = Thread(target=check).start()
answer = input("Input Something : ")
print(answer)
