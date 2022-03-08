🚧 under contruction 🚧 

# Computer Science CheetSheet
a quick guide and study notes for basic algorithms, datastructure, and etc. basically, my summary of algorithms for core comp sci classes i tooked at the college.
Python si used for the example codes.

# Author
me. -- If you find any mistakes (syntax, logic, or grammar), criticisms are always welcomed! Feel free to reach out to me here: choikj0903@gmail.com

# Table of Content
* [Programming Basics](#programming-basics)
* [Data Structure](#data-structure)
  * [Data Structure Basics](#data-structure-basics)
  * [Array](#array--list)
  * [Linked List](#linked-list)
  * [Stack](#stack)
  * [Queue](#queue)
* [Algorithm Basics](#algorithm-basics)
* [Search Algorithms](#search-algorithms)
  * [Linear Search](#linear-search--sequential-search)
  * [Binary Search](#binary-search)

# Programming Basics

# Data Structure

## Data Structure Basics
***Data Structure*** is a way of organizing data in a computer efficiently. Different data structures are used according to the purpose so that a computer can effectively load and store data.

***Abstract Data Type (ADT)*** is a data type described by pre-defined using user operation such as "insert data at the rear". ***ADT*** only provides what operations are defined, not how the operations are implemented. For example, ***Stack*** is a ***abstract data type***. ***Stack*** is defined by ***push()*** which inserts an element at the top of the stack and ***pop()*** which gets top-most element out of the stack.

## Array / List
***Array*** or ***List*** stores data in sequential order. Each element can be accessed using an **index** usually starting from 0.

Time Complexity:
* Indexing: O(1)
```python
a = ['a','b','c','d']

#indexing
print(a[2]) #prints 'c'
```


## Linked List
***Linked List*** is a series of entries that stores the value and a pointer to the next entry. Each entry is called ***Node***. Physical placement of the ***Nodes*** does not have to be sequential.

***Singly Linked List***: each Node has only one pointer pointing the next Node. Can only traverse in one direction.
***Doubly Linked List***: each Node has two pointers: one pointing to the next Node, another pointing to the previous Node. Can traverse in both direction.
***Circular Linked List***: "last" Node of the list points to the "first" Node of the list. Can traverse the list infinitely around the list.

Time Complexity:
* Indexing: O(N)
* Append/Prepend: O(1)
* Delete: O(N)

[Implementation](implementation/linked-list.py)


## Stack
**Stack** is a ADT that is described by Last-In-Fist-Out(LIFO) behavior. It can be implemented using both **Array** or **Linked List**
* ***push()***: insert an element at the top of the stack
* ***pop()***: return and remove an element at the top of the stack

[Implementation](#stack-1)

## Queue
**Queue** is a ADT that is described by First-In-First-Out(FIFO) behavior. It can be implemented using both **Array** or **Linked List**
* ***enque()***: insert an element at the end of the queue
* ***deque()***: return and remove an element at the head of queue

[Implementation](#stack-1)

## HashTable, HashMap

## Tree

## Binary Tree

## Binary Search Tree

## AVL Tree

## Graph


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
  
