# Linear Search

## Problem

Given an array and a target element, return the index of the target if it exists. Otherwise, return `-1`.

### Example

```python
array = [5, 10, 15, 20]
target = 15
```

**Output**

```python
2
```

---

## Idea

Traverse the array from left to right and compare each element with the target. Return the index when the target is found.

---

## Algorithm

1. Traverse the array.
2. Compare each element with the target.
3. If found, return its index.
4. If the loop ends, return `-1`.

---

## Python Implementation

```python
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

---

## Key Learning

- Sequential searching
- Array traversal
- Returning early when a match is found