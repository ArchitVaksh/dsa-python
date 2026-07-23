# Right Rotate Array by One Position

## Problem

Rotate an array to the right by one position.

---

## Idea

Traverse from right to left and repeatedly swap adjacent elements, moving the last element to the beginning.

---

## Algorithm

1. Start from the last index.
2. Swap the current element with the previous one.
3. Continue until index `1`.

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

---

## Key Learning

- Reverse traversal
- In-place rotation