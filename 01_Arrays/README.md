# Arrays

This folder contains my implementations of fundamental array algorithms in Python. These problems are helping me build a strong foundation in Data Structures and Algorithms.

---

# Algorithms Completed

- Linear Search
- Find Maximum Element
- Find Minimum Element
- Check if Array is Sorted

---

# 1. Linear Search

## Idea

Traverse the array one element at a time until the target is found.

## Algorithm

1. Start from the first element.
2. Compare each element with the target.
3. If found, return its index.
4. If the loop ends, return `-1`.

### Time Complexity

- Best Case: **O(1)**
- Average Case: **O(n)**
- Worst Case: **O(n)**

### Space Complexity

- **O(1)**

---

# 2. Find Maximum Element

## Idea

Assume the first element is the maximum, then compare it with every other element.

## Algorithm

1. Assume the first element is the maximum.
2. Traverse the array.
3. If a larger element is found, update the maximum.
4. Return the maximum element.

### Time Complexity

- Best Case: **O(n)**
- Average Case: **O(n)**
- Worst Case: **O(n)**

### Space Complexity

- **O(1)**

---

# 3. Find Minimum Element

## Idea

Assume the first element is the minimum, then compare it with every other element.

## Algorithm

1. Assume the first element is the minimum.
2. Traverse the array.
3. If a smaller element is found, update the minimum.
4. Return the minimum element.

### Time Complexity

- Best Case: **O(n)**
- Average Case: **O(n)**
- Worst Case: **O(n)**

### Space Complexity

- **O(1)**

---

# 4. Check if Array is Sorted

## Idea

Compare every element with its next element. If any element is greater than the next one, the array is not sorted.

## Algorithm

1. Traverse the array from the first element to the second last element.
2. Compare the current element with the next element.
3. If the current element is greater than the next one, return `False`.
4. If the loop finishes without finding any violation, return `True`.

### Time Complexity

- Best Case: **O(1)** *(when the first pair is unsorted)*
- Average Case: **O(n)**
- Worst Case: **O(n)**

### Space Complexity

- **O(1)**
