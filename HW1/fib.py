#fib.py

from functools import lru_cache
import csv
import time
from pathlib import Path

CSV_Path = Path("fib_timings.csv")

def timer(func):
    """A decorator that times the execution of a function."""
    
    # Initialize the CSV file with headers if it doesn't exist
    if not CSV_Path.exists():
        with open(CSV_Path, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["n", "result", "elapsed_time_sec"])
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Finished in {end_time - start_time:.8f}s: {func.__name__}({args[0]}) -> {result}")
        # Append the timing result to the CSV file
        with open(CSV_Path, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([args[0], result, end_time - start_time])
        return result
    return wrapper

@lru_cache
@timer
def fib(n: int) -> int:
    """Returns the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
if __name__ == "__main__":
    fib(100)
