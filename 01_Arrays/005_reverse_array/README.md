# Reverse an Array

## Problem

Reverse the elements of an array in-place.

### Example

```python
[1,2,3,4,5]
```

Output

```python
[5,4,3,2,1]
```

---

## Idea

Use two pointers starting from both ends and swap until they meet.

---

## Algorithm

1. Set left and right pointers.
2. Swap elements.
3. Move pointers inward.
4. Repeat until left >= right.

---

## Python Implementation

```python
def reverse_array(array):
    left = 0
    right = len(array)-1

    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    return array
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

---

## Key Learning

- Two-pointer technique
- In-place swapping