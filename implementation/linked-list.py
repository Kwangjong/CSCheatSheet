class Node:
  def __init__(self, val, p_next=None):
    self.val = val
    self.next = p_next

class LinkedList:
  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  def append(self, val): #O(1)
    if self.__size == 0:
      self.__head = Node(val)
      self.__tail = self.__head
   
    else:
      self.__tail.next = Node(val)
      self.__tail = self.__tail.next
      
    self.__size += 1

  def get(self, index): #O(n)
    if index >= self.__size:
      return None

    curr = self.__head
    while index > 0:
      curr = curr.next
      index -= 1

    return curr.val

  def delete(self, index): #O(n)
    if index >= self.__size:
      return True

    curr = self.__head
    while index > 1:
      curr = curr.next
      index -= 1
    curr.next = curr.next.next
    self.__size -= 1

    return False

  def size(self):
    return self.__size