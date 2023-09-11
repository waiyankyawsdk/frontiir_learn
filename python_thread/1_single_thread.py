from time import sleep, perf_counter

def task():
    print('Start a task')
    sleep(1)
    print('done')

start_time = perf_counter()

task()
task()

end_time = perf_counter()

print(f'It look {end_time - start_time: 0.2f} second(s) to complete.')