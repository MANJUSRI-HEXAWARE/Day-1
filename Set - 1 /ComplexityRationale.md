Introduction
I implemented five tasks based on a real-world online order management scenario. My objective was to apply different algorithms and data structures, test their performance, and understand their practical uses.

Task 1 – Order Searching
I implemented Linear Search and Binary Search to retrieve orders using Order ID from a dataset of 50,000
records.
I sorted the records before applying Binary Search and compared both algorithms based on execution time and number of comparisons.
• Time Complexity: Linear – O(n); Binary – O(log n).
• Space Complexity: Both – O(1) auxiliary space for searching.
• Rationale: I used Linear Search for direct record checking and Binary Search to reduce the search range and retrieve orders with fewer comparisons.

Task 2 – Order Sorting
I implemented Selection Sort and Merge Sort to arrange orders by amount in descending order. I traced the first three Selection Sort passes and compared both algorithms with Python's built-in sorting function using 10,000 records.
• Time Complexity: Selection Sort – O(n²); Merge Sort – O(n log n); Built-in Sort – O(n log n) worst case.
• Space Complexity: Selection Sort – O(n) in my implementation; Merge Sort – O(n); Built-in Sort – O(n).
• Rationale: I used Selection Sort to understand basic sorting and Merge Sort to achieve better efficiency with larger datasets. Built-in sorting was used for performance comparison.

Task 3 – Duplicate Order Detection
I implemented a Hash Map to identify duplicate orders using customer ID, amount, and creation date and minute. The program successfully identified repeated submissions in the dataset.
• Time Complexity: O(n) average case.
• Space Complexity: O(n).
• Rationale: I used hashing because it allows quick lookup of previously stored order details without comparing every record with all other records.

Task 4 – Stack and Queue
I created custom Stack and Queue implementations and compared them with Python's built-in List and Deque. I used Stack for undoing the last order edit and Queue for processing warehouse dispatches in arrival order.
• Time Complexity: Stack Push/Pop – O(1); Custom Queue Enqueue/Dequeue – O(1); Deque operations – O(1).
• Space Complexity: O(n) for both structures.
• Rationale: I selected Stack based on LIFO for undo operations and Queue based on FIFO for maintaining the correct dispatch sequence.

Task 5 – Refund Calculation
I implemented Greedy and Dynamic Programming approaches to calculate the minimum number of notes or coins required for a refund. I tested Indian currency denominations and demonstrated a case where Greedy fails using [1, 3, 4] for amount 6. Dynamic Programming produced the optimal combination [3, 3].
• Time Complexity: Greedy – O(d log d + k); Dynamic Programming – O(A × d).
• Space Complexity: Greedy – O(k); Dynamic Programming – O(A).
• Rationale: I used Greedy for its simple denomination-selection approach and Dynamic Programming to find the optimal solution when Greedy does not produce the minimum number of coins.
