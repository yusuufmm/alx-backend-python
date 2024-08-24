# Python Async Function Tasks

This project involves creating Python async functions to manage concurrent execution and measure runtime efficiency.

## Tasks Overview

### Task 1: Concurrent Coroutines

- **Function:** `wait_n(n, max_delay)`
- **Description:** Spawns `wait_random` n times and returns the list of delays in ascending order.

### Task 2: Measure Runtime

- **Function:** `measure_time(n, max_delay)`
- **Description:** Returns the average execution time for `wait_n(n, max_delay)`.

### Task 3: Create Task

- **Function:** `task_wait_random(max_delay)`
- **Description:** Returns an `asyncio.Task` for `wait_random` with the specified `max_delay`.

### Task 4: Task-Based Concurrent Coroutines

- **Function:** `task_wait_n(n, max_delay)`
- **Description:** Runs n tasks using `task_wait_random` and returns sorted delays.
