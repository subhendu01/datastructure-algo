### The Merge Sort Algorithm in Python
Merge sort is a very efficient sorting algorithm. It’s based on the divide-and-conquer approach, a powerful algorithmic technique used to solve complex problems.
To properly understand divide and conquer, you should first understand the concept of recursion. Recursion involves breaking a problem down into smaller subproblems until they’re small enough to manage. In programming, recursion is usually expressed by a function calling itself.

Divide-and-conquer algorithms typically follow the same structure:

    1.The original input is broken into several parts, each one representing a subproblem that’s similar to the original but simpler.
    2.Each subproblem is solved recursively.
    3.The solutions to all the subproblems are combined into a single overall solution.

In the case of merge sort, the divide-and-conquer approach divides the set of input values into two equal-sized parts, sorts each half recursively, and finally merges these two sorted parts into a single sorted list.

### Measuring Merge Sort’s Big O Complexity
To analyze the complexity of merge sort, you can look at its two steps separately:

    1. merge() has a linear runtime. It receives two arrays whose combined length is at most n (the length of the original input array), and it combines both arrays by looking at each element at most once. This leads to a runtime complexity of O(n).
    2. The second step splits the input array recursively and calls merge() for each half. Since the array is halved until a single element remains, the total number of halving operations performed by this function is log2n. Since merge() is called for each half, we get a total runtime of O(n log2n).
Interestingly, O(n log2n) is the best possible worst-case runtime that can be achieved by a sorting algorithm.