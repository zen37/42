# Highest Product of Two Numbers

This project compares three Python implementations for finding the highest product that can be made from any two integers in a list.

It also benchmarks the implementations and measures peak memory usage.

## Problem

Given a list of integers, return the highest product that can be made from any two numbers.

A correct solution must handle negative numbers, because two negative values can produce a large positive product.

Example:

```python
numbers = [-10, -3, 1, 2]
# highest product = (-10) * (-3) = 30
```

## Implementations

The project currently compares three approaches:

- `sorted()`
  - Sort the whole list.
  - Compare:
    - the product of the two largest values
    - the product of the two smallest values
- `one-pass islice`
  - Scan the list once.
  - Track the two largest and two smallest values.
  - Iterate with `itertools.islice(...)` instead of creating a sliced copy.
- `one-pass index`
  - Scan the list once.
  - Track the two largest and two smallest values.
  - Iterate using `range(...)` and index lookups.

## Why the one-pass solutions work

The highest product of two numbers can come from:

- the two largest positive numbers
- or the two most negative numbers

That is why the one-pass solutions track both extremes while scanning the list.

## Testing

The project includes automated tests with `pytest`.

Run tests with:

```bash
pytest
```

Use verbose mode if you want more detail:

```bash
pytest -v
```

## Benchmark methodology

Each implementation is benchmarked with the same randomly generated input for a given size.

The benchmark reports:

- result
- total wall-clock time
- average wall-clock time per run
- peak memory usage

### Important benchmarking lesson

At first, timing and memory were measured in the same benchmark run while `tracemalloc` was enabled.

That distorted the timing results.

Why:

- `tracemalloc` traces Python memory allocations
- tracing allocations adds overhead
- that overhead does not necessarily affect all implementations equally

In this project, the distortion was especially visible in the index-based version. Once time and memory were measured separately, the `one-pass index` implementation became much faster than the earlier combined benchmark suggested.

### Final benchmark design

The benchmark was refactored into two separate measurements:

- a timing run using `perf_counter()` only
- a memory run using `tracemalloc` only

This makes the time comparison fairer and the memory measurement clearer.

## Why `islice` was better than slicing

An earlier version used:

```python
for number in numbers[2:]:
```

That creates a new list containing almost the entire original list from index 2 onward.

It was later changed to:

```python
from itertools import islice

for number in islice(numbers, 2, None):
```

Why this is better:

- `numbers[2:]` creates a copy
- `islice(numbers, 2, None)` iterates lazily
- no large temporary list is created

### Result of this refactor

Switching from slicing to `islice` kept the one-pass approach fast while dramatically reducing memory usage.

In practice:

- speed stayed about the same
- peak memory dropped from several megabytes to almost nothing extra

This made the `one-pass islice` version the best overall trade-off in this project.

## Benchmark results

### 100 numbers, repeated 100000 times

```text
sorted()
result:        9595643028
wall total:    254.226 ms
wall average:  0.002542 ms per run
peak memory:   0.891 KB

one-pass islice
result:        9595643028
wall total:    305.816 ms
wall average:  0.003058 ms per run
peak memory:   0.117 KB

one-pass index
result:        9595643028
wall total:    342.131 ms
wall average:  0.003421 ms per run
peak memory:   0.109 KB

All methods returned the same result.
Fastest by wall time: sorted()
```

### 1,000 numbers, repeated 10000 times

```text
sorted()
result:        9946170278
wall total:    404.310 ms
wall average:  0.040431 ms per run
peak memory:   11.758 KB

one-pass islice
result:        9946170278
wall total:    242.447 ms
wall average:  0.024245 ms per run
peak memory:   0.117 KB

one-pass index
result:        9946170278
wall total:    324.293 ms
wall average:  0.032429 ms per run
peak memory:   0.145 KB

All methods returned the same result.
Fastest by wall time: one-pass islice
```

### 10,000 numbers, repeated 1000 times

```text
sorted()
result:        9998700036
wall total:    799.639 ms
wall average:  0.799639 ms per run
peak memory:   117.242 KB

one-pass islice
result:        9998700036
wall total:    230.409 ms
wall average:  0.230409 ms per run
peak memory:   0.117 KB

one-pass index
result:        9998700036
wall total:    334.718 ms
wall average:  0.334718 ms per run
peak memory:   0.145 KB

All methods returned the same result.
Fastest by wall time: one-pass islice
```

### 100,000 numbers, repeated 100 times

```text
sorted()
result:        9999700002
wall total:    1039.114 ms
wall average:  10.391141 ms per run
peak memory:   1171.781 KB

one-pass islice
result:        9999700002
wall total:    233.056 ms
wall average:  2.330556 ms per run
peak memory:   0.117 KB

one-pass index
result:        9999700002
wall total:    339.298 ms
wall average:  3.392978 ms per run
peak memory:   0.145 KB

All methods returned the same result.
Fastest by wall time: one-pass islice
```

### 1,000,000 numbers, repeated 10 times

```text
sorted()
result:        10000000000
wall total:    1437.639 ms
wall average:  143.763854 ms per run
peak memory:   11718.578 KB

one-pass islice
result:        10000000000
wall total:    237.492 ms
wall average:  23.749154 ms per run
peak memory:   0.117 KB

one-pass index
result:        10000000000
wall total:    344.365 ms
wall average:  34.436533 ms per run
peak memory:   0.145 KB

All methods returned the same result.
Fastest by wall time: one-pass islice
```

## Summary

Main takeaways from this project:

- all three implementations return the same result
- for very small input, `sorted()` can still win
- for larger inputs, the one-pass approaches are faster
- `one-pass islice` is the strongest overall option here
- measuring time and memory together with `tracemalloc` can distort performance results
- replacing list slicing with `itertools.islice` removed the large temporary copy and greatly reduced memory usage

## How to run

Run the benchmark script:

```bash
python main.py
```

Run the tests:

```bash
pytest
```
