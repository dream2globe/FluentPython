""" [예제 18-1] spinner_thread.py : 스레드로 텍스트 스피너 애니메이트하기 """
import threading
import itertools
import time
import sys

class Signal:
    go = True
    
def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status)) # 문자열 길이만큼 백스페이스를 반복해서 커서를 앞으로 이동시킴
        time.sleep(.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status)) # 스페이스로 기존 문자열을 지우고 백스페이스로 원래 위치로 돌아감
    
def slow_function():
    # 입출력을 위해 장시간 기다리는 것 처럼 보임
    time.sleep(15) # 주 스레드에서 sleep( ) 함수를 호출할 때 GIL이 해제되므로 두 번째 스레드가 진행됨
    return 42

def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin,
                               args=('thinking!', signal))
    print('spinner object:', spinner)
    spinner.start() # spinner 스레드 시작
    result = slow_function()
    signal.go = False
    spinner.join()  # spinner 스레드가 끝날 때 까지 기다림
    return result

def main():
    result = supervisor()
    print('Answer:', result)
    
if __name__ == '__main__':
    main()