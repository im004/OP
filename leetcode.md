# 🎯 Day 12 LeetCode Log: Arrays, Strings, and HashMaps

## Problem 1: Contains Duplicate (LeetCode 217)

- **Approach:** Used a `HashSet` to keep track of elements we have visited while iterating through the array. Checking existence in a set happens in constant time ($O(1)$).
- **Time Complexity:** $O(n)$ — Single pass loop through the input array of size $n$.
- **Space Complexity:** $O(n)$ — In the worst-case scenario where all elements are unique, the set will store all $n$ items.
- **Did I solve it alone?** Yes, solved from memory and logic.
- **What I learned:** Sets are the absolute fastest tool when the core problem boils down to checking if an item has been seen before.

---

## Problem 2: Valid Anagram (LeetCode 242)

- **Approach:** Created two separate frequency maps (dictionaries) using Python's `.get(char, 0) + 1` pattern to count occurrences of each letter. Added an early exit check to compare string lengths.
- **Time Complexity:** $O(n)$ — Iterating through each string of length $n$ to tally elements takes linear time.
- **Space Complexity:** $O(1)$ — Although dictionaries are used, the space is bounded by the size of the alphabet (maximum 26 unique character keys), which is constant.
- **Did I solve it alone?** Yes, referenced past code notes to nail the `.get()` syntax.
- **What I learned:** Dictionary equivalence `==` in Python checks keys and value balances automatically, avoiding manual loops. The `.get(key, default)` method eliminates tedious `if/else` checks for non-existent keys.

---

## Problem 3: Two Sum (LeetCode 1)

- **Approach:** Used a `HashMap` to store values and their index mappings. For each item, we calculated the required `complement` ($target - current$). If the complement exists in our map, we immediately return the pair of indices.
- **Time Complexity:** $O(n)$ — We pass through the list exactly once, performing constant time dictionary lookups.
- **Space Complexity:** $O(n)$ — In the worst case, we store up to $n$ elements in the dictionary.
- **Did I solve it alone?** Yes, except for fixing a minor case typo (`seen[current] = i` instead of a capital `I`).
- **What I learned:** Instead of using nested loops ($O(n^2)$), trading a bit of memory space ($O(n)$ hashmap) allows us to lower the runtime complexity down to linear time.

---

## Problem 4: Maximum Subarray (LeetCode 53)

- **Approach:** Implemented Kadane's Algorithm. We track the `current_sum` and `max_sum` simultaneously. At each element, the code evaluates whether it's better to add the element to the running sum or throw away the history and start fresh: `max(num, current_sum + num)`.
- **Time Complexity:** $O(n)$ — A single pass loop checks each number in the array once.
- **Space Complexity:** $O(1)$ — Only tracking two numeric variables regardless of input scaling.
- **Did I solve it alone?** No, folded and reviewed the official solution strategy.
- **What I learned:** Starting local counters at `nums[0]` rather than `0` is vital for arrays containing only negative integers. Kadane’s is the ultimate pattern for finding the maximum contiguous window.

---

## Problem 5: Climbing Stairs (LeetCode 70)

- **Approach:** Upgraded the problem into an iterative Dynamic Programming/Fibonacci problem. The logic follows that the number of ways to reach step $n$ is the sum of choices from step $n-1$ and step $n-2$. Used a sliding window variables array to step forward.
- **Time Complexity:** $O(n)$ — The `for` loop executes operations from step 3 up to $n$.
- **Space Complexity:** $O(1)$ — Used variable state tracking (`one_step_behind`, `two_steps_behind`) to avoid the heavy memory footprint of recursion stacks.
- **Did I solve it alone?** No, studied the solution pattern to construct the final step logic loop.
- **What I learned:** Complex scaling problems can be broken down into simpler base blocks. If the combinations for state $n$ explicitly depend on state $n-1$, look for sliding window or array-caching patterns.

---

## 📊 Core Pattern Summary

| Pattern / Recognition Signal                   | Applied Problems   | Key Architecture                |
| :--------------------------------------------- | :----------------- | :------------------------------ |
| **HashSet Tracking** (`"Seen before?"`)        | Contains Duplicate | `set()` lookup / insertion      |
| **HashMap Frequency** (`"Count of X?"`)        | Valid Anagram      | `dict.get(key, 0) + 1`          |
| **HashMap Complement** (`"Target Pair?"`)      | Two Sum            | Looking up `target - current`   |
| **Kadane's Algorithm** (`"Best window?"`)      | Maximum Subarray   | `max(num, current_sum + num)`   |
| **Dynamic Programming** (`"Subproblem build"`) | Climbing Stairs    | Memoization/Baton sliding loops |
