### Measuring Insertion Sort’s Big O Runtime Complexity
Similar to bubble sort implementation, the insertion sort algorithm has a couple of nested loops that go over the list. The inner loop is pretty efficient because it only goes through the list until it finds the correct position of an element. That said, the algorithm still has an O(n2) runtime complexity on the average case.
The worst case happens when the supplied array is sorted in reverse order. In this case, the inner loop has to execute every comparison to put every element in its correct position. This still gives you an O(n2) runtime complexity.
The best case happens when the supplied array is already sorted. Here, the inner loop is never executed, resulting in an O(n) runtime complexity, just like the best case of bubble sort.
Although bubble sort and insertion sort have the same Big O runtime complexity, in practice, insertion sort is considerably more efficient than bubble sort. If you look at the implementation of both algorithms, then you can see how insertion sort has to make fewer comparisons to sort the list.

### Analyzing the Strengths and Weaknesses of Insertion Sort
Just like bubble sort, the insertion sort algorithm is very uncomplicated to implement. Even though insertion sort is an O(n2) algorithm, it’s also much more efficient in practice than other quadratic implementations such as bubble sort.
There are more powerful algorithms, including merge sort and quicksort, but these implementations are recursive and usually fail to beat insertion sort when working on small lists. Some quicksort implementations even use insertion sort internally if the list is small enough to provide a faster overall implementation. Timsort also uses insertion sort internally to sort small portions of the input array.
That said, insertion sort is not practical for large arrays, opening the door to algorithms that can scale in more efficient ways.

### for more info
https://realpython.com/sorting-algorithms-python/