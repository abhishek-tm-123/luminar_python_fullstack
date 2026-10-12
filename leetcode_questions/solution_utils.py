
import time
from functools import wraps


def test_solution(test_cases):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"\nTesting: {func.__name__}")
            passed = 0
            total_time = 0.0

            for inputs, expected in test_cases:
                start = time.perf_counter()

                try:
                    actual = func(inputs)
                    elapsed = (time.perf_counter() - start) * 1000
                    total_time += elapsed

                    if actual == expected:
                        passed += 1
                        status = "PASS"
                    else:
                        status = "FAIL"

                    print(
                        f"{status} | Input: {inputs} | "
                        f"Expected: {expected} | Actual: {actual} | "
                        f"Time: {elapsed:.4f} ms"
                    )

                except Exception as error:
                    elapsed = (time.perf_counter() - start) * 1000
                    total_time += elapsed
                    print(
                        f"ERROR | Input: {inputs} | "
                        f"{type(error).__name__}: {error}"
                    )

            print(f"\nPassed: {passed}/{len(test_cases)}")
            print(f"Total execution time: {total_time:.4f} ms")

            # Execute normally with the arguments provided by the caller.
            return func(*args, **kwargs)

        return wrapper
    return decorator
