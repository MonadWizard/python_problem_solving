# Hashing Data Structure: Key Concepts and Complete Guide

Hashing is a **fundamental data structure concept** used to achieve **fast access, insertion, and deletion**.  
It is based on the idea of mapping **keys → indices** in a fixed-size array (hash table).

---

## 🔑 Key Concepts of Hashing

1. **Hash Function**  
   - Converts a key into an array index.  
   - Must be **deterministic**, **fast**, and distribute keys **uniformly**.

2. **Hash Table**  
   - An array where data is stored at indices computed by the hash function.

3. **Bucket**  
   - Each index of the hash table is a bucket.  
   - Buckets may store one or more elements (if collisions happen).

4. **Collision**  
   - When two keys map to the same bucket.  
   - Requires resolution strategies.

5. **Load Factor (α)**  
   - Ratio: `Number of Elements / Table Size`.  
   - Determines when to **rehash** (resize table).

6. **Rehashing**  
   - Expanding table size and redistributing elements to reduce collisions.

7. **Applications**  
   - Symbol tables (compilers)  
   - Databases (indexes)  
   - Caches (LRU Cache, Redis)  
   - Python’s `dict` and `set`  

---

## ⏱️ Complexity of Hashing

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search    | O(1)         | O(n)       |
| Insert    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |

- **Average Case** → With good hash function and low load factor.  
- **Worst Case** → Many collisions (all keys in one bucket).

---

## 🔢 Hash Functions in Detail

### 1. Numbers
- Use modulus operator:  
  ```python
  index = key % table_size
  ```

### 2. Characters (ASCII Code)
- Each character has an ASCII value.  
  ```python
  index = ord(ch) % table_size
  ```
- Example: 'A'=65, 'B'=66, 'a'=97.

### 3. Strings (Polynomial Rolling Hash)
- Combine ASCII values using polynomial expansion.  
  ```python
  def string_hash(s, table_size, base=31, mod=10**9+9):
      h = 0
      for ch in s:
          h = (h * base + ord(ch)) % mod
      return h % table_size
  ```

---

## 🧑‍💻 Python Examples

### Example 1: Number Hashing
```python
def number_hashing(numbers, table_size):
    table = [[] for _ in range(table_size)]
    for num in numbers:
        index = num % table_size
        table[index].append(num)
    return table

print(number_hashing([15, 11, 27, 8, 12], 7))
```

**Step Result**:
- 15 % 7 = 1 → bucket[1] = [15]  
- 11 % 7 = 4 → bucket[4] = [11]  
- 27 % 7 = 6 → bucket[6] = [27]  
- 8 % 7 = 1 → bucket[1] = [15, 8] (collision)  
- 12 % 7 = 5 → bucket[5] = [12]  

---

### Example 2: Character Hashing (ASCII)
```python
def char_hashing(chars, table_size):
    table = [[] for _ in range(table_size)]
    for ch in chars:
        index = ord(ch) % table_size
        table[index].append((ch, ord(ch)))
    return table

print(char_hashing(['A', 'B', 'a', 'z', 'k'], 7))
```

**Step Result**:
- 'A'=65 → 65 % 7 = 2 → bucket[2] = ['A']  
- 'B'=66 → 66 % 7 = 3 → bucket[3] = ['B']  
- 'a'=97 → 97 % 7 = 6 → bucket[6] = ['a']  
- 'z'=122 → 122 % 7 = 3 → bucket[3] = ['B','z'] (collision)  
- 'k'=107 → 107 % 7 = 2 → bucket[2] = ['A','k'] (collision)  

---

## ⚔️ Collision Handling

1. **Chaining** (store multiple items in lists per bucket).  
2. **Open Addressing** (find another empty slot):  
   - Linear Probing: `(i+1) % table_size`.  
   - Quadratic Probing: `(i+j^2) % table_size`.  
   - Double Hashing: use another hash function.  
3. **Rehashing**: Increase table size & redistribute.

---

## 📊 Load Factor

\[ α = \frac{\text{Number of Elements}}{\text{Table Size}} \]

- If `α > 0.7`, collisions increase → rehash.  
- Example: 14 elements in table of size 20 → α = 0.7.

---

## 🧮 Multiplicative Perfect Hashing (MPP)

Formula:  
\[ h(key) = \lfloor table\_size \times ((key \times A) \, mod \, 1) \rfloor \]  

Where `A` is a constant (0.6180339887 – golden ratio).

```python
def multiplicative_hash(key, table_size, A=0.6180339887):
    return int(table_size * ((key * A) % 1))

print([multiplicative_hash(x, 10) for x in [10, 20, 30, 40]])
```

---

## 📦 Unordered Map

- **C++** → `unordered_map` uses hashing.  
- **Python** → `dict` and `set` use hash tables internally.

```python
# Dict as hash map
marks = {"Alice": 90, "Bob": 85}
print(marks["Alice"])  # O(1)

# Set as hash set
unique = {1, 2, 3}
print(2 in unique)  # O(1)
```

---

## ⚠️ Limitations of Hashing
- Collisions are **inevitable**.  
- No inherent **ordering** of elements.  
- Memory overhead for sparse tables.  
- Poor hash function → clustering and O(n) performance.

---

## 📌 Summary
- Hashing = **keys → indices** using hash functions.  
- Supports **O(1) average** operations.  
- Collisions require handling (chaining / probing).  
- Load factor determines when to resize.  
- Used everywhere: compilers, DBs, caches, Python dict/set.  

---
