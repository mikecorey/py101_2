import time

def slow_check():
    time.sleep(5)
    return False

def fast_check():
    return False

print('start')
if fast_check() and slow_check():
    print('not reachable')

print('done')
