from time import sleep, perf_counter
from threading import Thread

def task():
    print('Starting a task')
    sleep(2)
    print('done')

start_time = perf_counter()

t1 = Thread(target=task)
t2 = Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = perf_counter()
print(f'It look {end_time - start_time : 0.2f} second(s) to complete.')
