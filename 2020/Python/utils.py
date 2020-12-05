"""Helper functions to handle data. Run files at root directory level."""
import typing
import json
import time

def get_data(key: str) -> typing.Any:
  with open("2020/inputs.json", "r") as f:
    data = json.load(f)[key] 
  return data

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f'Time Taken: {time.perf_counter() - start}')
        return result
    return wrapper

def avg_timer(run: int=10):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            times = []
            for i in range(run):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                times.append(end - start)
            print(f"Average time over {run} runs: {sum(times)/run}")
            return result
        return inner_wrapper
    return wrapper 

def avg_timer_ns(run: int=10):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            times = []
            for i in range(run):
                start = time.perf_counter_ns()
                result = func(*args, **kwargs)
                end = time.perf_counter_ns()
                times.append(end - start)
            print(f"Average time over {run} runs: {sum(times)/run} ns")
            return result
        return inner_wrapper
    return wrapper

            

                