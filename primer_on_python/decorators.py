import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args,**kwargs):
        #Do something before
        value = func(*args,**kwargs)
        #Do something after
        return value
    return wrapper_do_twice

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1 create a list of positional args.repr():to get nice string for each arg
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2 f-string format
        signature = ", ".join(args_repr + kwargs_repr)           # 3 arg+kwargs by seperating with comma
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4 return value is printed
        return value
    return wrapper_debug

import time
def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

#
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2 measuring time intervals
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat
