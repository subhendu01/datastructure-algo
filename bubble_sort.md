# datastructure_algo
### Measuring Bubble Sort’s Big O Runtime Complexity
Your implementation of bubble sort consists of two nested for loops in which the algorithm performs n - 1 comparisons, then n - 2 comparisons, and so on until the final comparison is done. This comes at a total of (n - 1) + (n - 2) + (n - 3) + … + 2 + 1 = n(n-1)/2 comparisons, which can also be written as ½n2 - ½n.

You learned earlier that Big O focuses on how the runtime grows in comparison to the size of the input. That means that, in order to turn the above equation into the Big O complexity of the algorithm, you need to remove the constants because they don’t change with the input size.

Doing so simplifies the notation to n2 - n. Since n2 grows much faster than n, this last term can be dropped as well, leaving bubble sort with an average- and worst-case complexity of O(n2).

In cases where the algorithm receives an array that’s already sorted—and assuming the implementation includes the already_sorted flag optimization explained before—the runtime complexity will come down to a much better O(n) because the algorithm will not need to visit any element more than once.

O(n), then, is the best-case runtime complexity of bubble sort. But keep in mind that best cases are an exception, and you should focus on the average case when comparing different algorithms.

### for more info
https://realpython.com/sorting-algorithms-python/
