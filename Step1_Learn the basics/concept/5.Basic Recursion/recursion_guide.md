# A Friendly Guide to Recursion (with Python examples)

Recursion is a programming technique where a function calls **itself** to solve a problem by reducing it into smaller subproblems. It's powerful for problems that have a natural “self‑similar” structure—like trees, divide‑and‑conquer algorithms, and many math sequences.

---

## Table of Contents
- [A Friendly Guide to Recursion (with Python examples)](#a-friendly-guide-to-recursion-with-python-examples)
  - [Table of Contents](#table-of-contents)
  - [What is Recursion?](#what-is-recursion)
  - [Base Condition (Base Case)](#base-condition-base-case)
  - [Stack Space \& Stack Overflow](#stack-space--stack-overflow)
  - [Recursion Tree](#recursion-tree)
  - [Python Demo Code (with deep explanations)](#python-demo-code-with-deep-explanations)
    - [1) Sum of an Array](#1-sum-of-an-array)
    - [2) Factorial](#2-factorial)
    - [3) Fibonacci](#3-fibonacci)
    - [4) Binary Search (Divide and Conquer)](#4-binary-search-divide-and-conquer)
    - [5) DFS on a Tree](#5-dfs-on-a-tree)
  - [When to Use Recursion vs Iteration](#when-to-use-recursion-vs-iteration)
  - [Common Pitfalls \& Tips](#common-pitfalls--tips)
    - [Quick Checklist for Any Recursive Function](#quick-checklist-for-any-recursive-function)

---

## What is Recursion?

> **Definition:** A function that solves a problem by calling itself on a smaller input, until it reaches an easy-to-solve situation (the **base case**).

**Core idea:** Solve `F(n)` by using the same function on smaller input(s) like `F(n-1)`, `F(n/2)`, etc., and combine the results.

**Pattern:**

```python
def fn(n):
    # 1) Base case — stop condition
    if small_enough(n):
        return easy_answer(n)

    # 2) Work + recursive call(s) — reduce the problem
    smaller = shrink(n)
    partial = fn(smaller)

    # 3) Combine results
    return combine(partial, n)
```

---

## Base Condition (Base Case)

A **base case** is a condition that **does not** rely on further recursion. It prevents infinite recursion and starts the chain of returns.

- Without a base case → recursion never stops → **stack overflow**.
- Often, the base case is the “smallest input” (e.g., empty list, `n == 0` or `n == 1`).

**Example:** In factorial, `0! = 1` is the base case.

---

## Stack Space & Stack Overflow

Every function call in Python creates a **stack frame** (local variables, return address). Recursion consumes one stack frame **per level**.

- **Stack space:** the memory consumed by the active chain of calls.
- **Depth of recursion:** how many nested calls are active before returns begin.
- **Stack overflow:** if recursion goes too deep, Python raises a `RecursionError` (by default around ~1000 frames). You can check or change the limit with `sys.getrecursionlimit()` / `sys.setrecursionlimit()`, but increasing it **blindly is risky**.

**Rule of thumb:** Prefer algorithms with **O(log n)** or **O(n)** recursion depth, or convert to iteration if depth could be very large.

---

## Recursion Tree

A **recursion tree** visualizes how a recursive function expands into subcalls and how results combine.

- **Linear recursion** (e.g., sum of array) creates a **single chain** of calls.
- **Branching recursion** (e.g., Fibonacci) creates a **tree** of calls, often duplicating work.

**Example (Fibonacci):**

```
fib(4)
├─ fib(3)
│  ├─ fib(2)
│  │  ├─ fib(1) -> 1
│  │  └─ fib(0) -> 0
│  └─ fib(1) -> 1
└─ fib(2)
   ├─ fib(1) -> 1
   └─ fib(0) -> 0
```

This tree has repeated subproblems (`fib(2)`, `fib(1)`), which leads to exponential time if not optimized.

---

## Python Demo Code (with deep explanations)

### 1) Sum of an Array

**Problem:** Return the sum of all numbers in a list.

**Recursive idea:** Sum of `arr[0:]` is `arr[0] + sum(arr[1:])`. Base case: empty list → 0.

```python
def sum_array(arr):
    # Base case
    if not arr:                # empty list
        return 0

    # Recursive case
    head = arr[0]
    tail = arr[1:]
    return head + sum_array(tail)
```

**Why it terminates:** Each call reduces the list length by 1 ⇒ eventually becomes empty.

**Time complexity:** O(n) (n calls)  
**Space complexity (stack):** O(n) (chain of n frames)

**Dry run:** `sum_array([3, 5, 2])`
```
= 3 + sum_array([5, 2])
= 3 + (5 + sum_array([2]))
= 3 + (5 + (2 + sum_array([])))
= 3 + 5 + 2 + 0
= 10
```

---

### 2) Factorial

**Definition:** `n! = n × (n-1) × (n-2) × ... × 1` or

**Factorial means** the product of all positive integers up to `n`.

`n! = n × (n-1)!` with base case `0! = 1`.

```python
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):        # base cases
        return 1
    return n * factorial(n - 1)
```

**Depth:** `n`  
**Time:** O(n)  
**Space (stack):** O(n)

> **Tail recursion?** Python does **not** optimize tail recursion, so writing tail-recursive factorial won’t save stack space.

---

### 3) Fibonacci

**Definition:** `fib(0) = 0`, `fib(1) = 1`, `fib(n) = fib(n-1) + fib(n-2)`

**Fibonacci means** the nth number in the sequence starting with 0 and 1. In detail, the sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... 

**Naive recursion (exponential time):**

```python
def fib_slow(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)
```

- **Time:** O(φ^n) (exponential)  
- **Space (stack):** O(n) (height of tree)

**Optimized with memoization (top‑down DP):**

***memoization means caching results of expensive function calls and reusing them when the same inputs occur again.***

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

- **Time:** O(n)  
- **Space:** O(n) for cache + O(n) stack

**Iterative (bottom‑up):** No recursion, O(1) extra space.

```python
def fib_iter(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

---

### 4) Binary Search (Divide and Conquer)

**Idea:** Repeatedly halve the search space. Works on **sorted** arrays.

```python
def binary_search(arr, target, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1

    # Base case: not found
    if lo > hi:
        return -1

    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, hi)
    else:
        return binary_search(arr, target, lo, mid - 1)
```

**Depth:** O(log n) (excellent for stack)  
**Time:** O(log n)

---

### 5) DFS on a Tree

Recursion matches tree structure naturally. Here is a pre‑order traversal (node → left → right).

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    result = []
    def dfs(node):
        if not node:                  # base case
            return
        result.append(node.val)       # visit
        dfs(node.left)                # left subtree
        dfs(node.right)               # right subtree
    dfs(root)
    return result
```

**Depth:** equals the tree height `h`  
**Time:** O(n) (visits each node once)  
**Space (stack):** O(h)

**Example tree and recursion tree are the same structure:**

```
        A
       /       B   C
     / \       D   E   F

preorder -> A, B, D, E, C, F
```

---

## When to Use Recursion vs Iteration

Use **recursion** when:
- The problem has a natural recursive structure (trees, divide‑and‑conquer).
- The recursion depth is small or bounded (like O(log n)).
- Code clarity is a priority and performance is acceptable.

Prefer **iteration** when:
- Depth could be large (risking stack overflow).
- Tail recursion would be needed for efficiency (Python can’t optimize it).
- You want tight control over memory and performance.

---

## Common Pitfalls & Tips

1. **Missing or incorrect base case** → infinite recursion.
2. **Not reducing input** each step → never reaches base case.
3. **Excessive branching** (like naïve Fibonacci) → exponential time; use memoization or bottom‑up DP.
4. **Slicing lists** (`arr[1:]`) copies list segments → extra O(n²) time over all calls; consider passing indices to avoid copying:
   ```python
   def sum_array_i(arr, i=0):
       if i == len(arr):
           return 0
       return arr[i] + sum_array_i(arr, i + 1)
   ```
5. **Stack depth risk**: convert to loops when necessary.

---

### Quick Checklist for Any Recursive Function
- ✅ Clear **base case(s)** that definitely trigger.
- ✅ Each call **reduces** the problem.
- ✅ Understand the **maximum depth** and whether it’s safe.
- ✅ Consider an **iterative** or **memoized** alternative if needed.
- ✅ Reason about **time/space complexity** and duplication of work.

---

*Happy recursing!* ✨
