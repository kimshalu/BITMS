def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:", arr)


'''

Here's how selection sort works step by step:

Selection of Smallest Element:
Start by finding the smallest element in the array.
Swap with First Element:
Swap the smallest element found with the first element of the array.
Repeat:
Repeat the process for the remaining part of the array
(excluding the first element).
Continue Selection:
Continue this process, each time finding the smallest
element from the unsorted portion and swapping it with the first unsorted element.
Sorted Portion: The sorted portion of the array grows incrementally
from left to right.

7,2,4,1,5

Step 1: Find the smallest element. In this case, it's 1.
Swap 1 with the first element. Now the array becomes: 
1
,
2
,
4
,
7
,
5
1,2,4,7,5
Step 2: Repeat the process for the remaining part of the array (
2
,
4
,
7
,
5
2,4,7,5).
Find the smallest element, which is 2.
Swap 2 with the second element. Now the array becomes: 
1
,
2
,
4
,
7
,
5
1,2,4,7,5
Step 3: Repeat the process for the remaining part of the array (
4
,
7
,
5
4,7,5).
Find the smallest element, which is 4.
Swap 4 with the third element. Now the array becomes: 
1
,
2
,
4
,
7
,
5
1,2,4,7,5
Step 4: Repeat the process for the remaining part of the array (
7
,
5
7,5).
Find the smallest element, which is 5.
Swap 5 with the fourth element. Now the array becomes: 
1
,
2
,
4
,
5
,
7
1,2,4,5,7

'''
