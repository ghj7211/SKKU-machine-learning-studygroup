import threading
import msvcrt

def getkey(): #단일키 입력
    return msvcrt.getch()

def start_timer(count, time):
    count += 1
    print(count)
    timer = threading.Timer(1,start_timer, args=[count, time])
    timer.start()

    if count == time:
        print('stop')
        timer.cancel()

start_timer(0,5)

