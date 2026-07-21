# Left Rotate Array by One Position

## Problem

Rotate an array to the left by one position.

---

## Idea

Traverse from left to right and repeatedly swap adjacent elements, moving the first element to the end.

---

## Algorithm

1. Traverse from index `1`.
2. Swap the current element with the previous one.
3. Continue until the last index.

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

---

## Key Learning

- Adjacent swapping
- In-place rotation