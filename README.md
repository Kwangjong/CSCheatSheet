🚧 under contruction 🚧 

# Algorithms CheetSheet
a quick guide and study notes for basic algorithms. basically, my summary of algorithms for core comp sci classes i tooked at the college.

## Author
me. -- If you find any mistakes (syntax, logic, or grammar), criticisms are always welcomed! Feel free to reach out to me here: choikj0903@gmail.com

## Table of Content
* [Algorithm Basics](#algorithm-basics)
  * [Iterative Algorithms](#iterative-algorithm)
  * [Recursive Algorithms](#recursive-algorithm)
* [Search Algorithms](#search-algorithms)
  * [Linear Search](#linear-search--sequential-search)
  * [Binary Search](#binary-search)

## Algorithm Basics
### Iterative Algorithm
An algorithm that performs number of steps repeatedly for a finite number of times. 
* Each repetition is called **iteration**.
* Uses looping statement like **for** and **while**.
* Mostly used to move through a data set like an array or a list. 


### Recursive Algorithm
An algorithm that calls itself.
* Recursive alorithm is divided into two parts: a **recursive case** and a **base case**.
* **Recursive case** is a condition where a recursion is triggered.
* **Base case** is a condition that stops the recursion and evaluates the result.
* Often used in Depth First Search

## Search Algorithms
### Linear Search / Sequential Search
A very simple searching algorithm. It starts from one end checking every element until the desired element is found.
* It can be performed in an unsorted list.
* Time Complexity : **O(n)**
```python
def LinearSearch(array, key):
  for i, elem in enumerate(array):
    if(array[i] == key):
      return i
      
  return -1
```

### Binary Search
A search algorithm that repeatedly divides the search interval in half until the desired element is found or the interval is empty.
* It can only be performed in a sorted list.
* Time Complexity : **O(log n)**
```python
def LinearSearch(array, key):
  left = 0
  right = len(array)
  mid = 0

  while left <= right:
    mid = (left+right) // 2

    if array[mid] < key:
      left = mid + 1
    
    elif array[mid] > key:
      right = mid - 1

    else:
      return mid

  return -1
 ```
  
