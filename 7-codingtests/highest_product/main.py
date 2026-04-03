from dataclasses import dataclass
from random import randint
from time import perf_counter
import tracemalloc


@dataclass
class BenchmarkResult:
    """Benchmark results for one method."""

    method_name: str
    result: int
    total_wall_ms: float
    average_wall_ms: float
    peak_memory_kb: float


def highest_product_sort(numbers: list[int]) -> int:
    """Return the highest product of any two numbers using sorting."""
    if len(numbers) < 2:
        raise ValueError("Need at least 2 numbers")

    sorted_numbers = sorted(numbers)
    return max(
        sorted_numbers[-1] * sorted_numbers[-2],
        sorted_numbers[0] * sorted_numbers[1],
    )


def highest_product_slice(numbers: list[int]) -> int:
    """Return the highest product of any two numbers using one pass and slicing."""
    if len(numbers) < 2:
        raise ValueError("Need at least 2 numbers")

    largest = max(numbers[0], numbers[1])
    second_largest = min(numbers[0], numbers[1])
    smallest = min(numbers[0], numbers[1])
    second_smallest = max(numbers[0], numbers[1])

    for number in numbers[2:]:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number

        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif number < second_smallest:
            second_smallest = number

    return max(largest * second_largest, smallest * second_smallest)


def highest_product_index(numbers: list[int]) -> int:
    """Return the highest product of any two numbers using one pass and indexing."""
    if len(numbers) < 2:
        raise ValueError("Need at least 2 numbers")

    largest = max(numbers[0], numbers[1])
    second_largest = min(numbers[0], numbers[1])
    smallest = min(numbers[0], numbers[1])
    second_smallest = max(numbers[0], numbers[1])

    for index in range(2, len(numbers)):
        number = numbers[index]

        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number

        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif number < second_smallest:
            second_smallest = number

    return max(largest * second_largest, smallest * second_smallest)


def generate_test_data(
    size: int, minimum: int = -100_000, maximum: int = 100_000
) -> list[int]:
    """Return a list of random integers for benchmarking."""
    return [randint(minimum, maximum) for _ in range(size)]


def benchmark(
    function, method_name: str, numbers: list[int], repeats: int
) -> BenchmarkResult:
    """Measure wall time and peak memory for one method."""
    tracemalloc.start()
    tracemalloc.reset_peak()

    wall_start = perf_counter()

    for _ in range(repeats):
        result = function(numbers)

    wall_end = perf_counter()

    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    total_wall_ms = (wall_end - wall_start) * 1000
    average_wall_ms = total_wall_ms / repeats
    peak_memory_kb = peak_bytes / 1024

    return BenchmarkResult(
        method_name=method_name,
        result=result,
        total_wall_ms=total_wall_ms,
        average_wall_ms=average_wall_ms,
        peak_memory_kb=peak_memory_kb,
    )


def print_benchmark_report(
    size: int, repeats: int, results: list[BenchmarkResult]
) -> None:
    """Print the benchmark results for all methods."""
    print(f"\nTesting with {size:,} numbers, repeated {repeats} times")
    print()

    for benchmark_result in results:
        print(benchmark_result.method_name)
        print(f"{'result:':<15}{benchmark_result.result}")
        print(f"{'wall total:':<15}{benchmark_result.total_wall_ms:.3f} ms")
        print(f"{'wall average:':<15}{benchmark_result.average_wall_ms:.6f} ms per run")
        print(f"{'peak memory:':<15}{benchmark_result.peak_memory_kb:.3f} KB")
        print()

    all_results_match = all(
        benchmark_result.result == results[0].result for benchmark_result in results
    )

    if all_results_match:
        print("All methods returned the same result.")
    else:
        print("Results do not match. Check the implementations.")

    fastest = min(results, key=lambda benchmark_result: benchmark_result.total_wall_ms)
    print(f"Fastest by wall time: {fastest.method_name}")
    print("--------------------------------------")


if __name__ == "__main__":
    sizes_and_repeats = [
        (100, 100_000),
        (1_000, 10_000),
        (10_000, 1_000),
        (100_000, 100),
        (1_000_000, 10),
    ]

    methods = [
        ("sorted()", highest_product_sort),
        ("one-pass slice", highest_product_slice),
        ("one-pass index", highest_product_index),
    ]

    for size, repeats in sizes_and_repeats:
        numbers = generate_test_data(size)

        results = [
            benchmark(function, method_name, numbers, repeats)
            for method_name, function in methods
        ]

        print_benchmark_report(size, repeats, results)
