class SinglyLinkedList:
  """LIFO Stack implementation using a singly linked list for storage."""

 #-------------------------- nested _Node class --------------------------
  class _Node:         # "inner" class
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'           # streamline memory usage

    def __init__(self, element, next):        # initialize node's fields
        self._element = element               # reference to user's element
        self._next = next                     # reference to next node

    def setNext(self, next):
        self._next = next
    
    def getNext(self):
        return self._next
  
    def setElement(self, element):
        self.element = _element
    
    def getElement(self):
        return self._element
        
  #------------------------------- stack methods -------------------------------
  def __init__(self, head = None, size = 0):
    """Create an empty list."""
    self._head = head                       # reference to the head node
    self._size = size                       # number of stack elements

  def getSize(self):
    """Return the number of elements in the list."""
    return self._size

  def isEmpty(self):
    """Return True if the list is empty."""
    return self._size == 0

  def add (self, element):
    """Add element element to the end of the list."""
    node = self._Node(element, None)
    if self.isEmpty():
        self._head = node
    else:
        cursor = self._head
        while cursor.getNext() is not None:
            cursor = cursor.getNext( )
        cursor.setNext(node)
    print('Adding # ', self._size, ' element: ', node.getElement())
    self._size += 1
        
  def remove(self):
    """Remove the element at the head of the list. Raise Empty if the list is empty."""
    if self.isEmpty():
      raise Empty('List is empty')
    self._size -= 1
    out = self._head.getElement()      # save the head element and return to the caller
    self._head = self._head.getNext()  # Reset the head to the second (next) list element
    return out

  def showList(self):
    """Display the contents of the list, from head to tail. Raise Empty exception if the List is empty. """
    if not self.isEmpty():
        cursor = self._head
        while True:
            print(cursor.getElement(), ' reference: ', id(cursor), id(cursor.getNext()))
            if cursor.getNext() == None: break
            cursor = cursor.getNext()
    return
        
  def search(self, key):
    """ Search the list looking for a node element = key. return True if found. """        
    cursor = self._head      # start search at head - set loop pointer cursor to head
    while cursor:
        if key == cursor.getElement():
            return True
        cursor = cursor.getNext()    # point at next node - reset cursor next
    return False

  def insertAfter (self, i, element):
    """Insert an element after the ith element of the list."""
    node = self._Node(element, None)
  # insert method body below
  # Cases: (1) insert into empty list, (2) insert before the head, (3) insert in the interior
    if self.isEmpty():
        self._head = node
    else:
        cursor = self._head
        if i == 1:
            node.setNext(self._head)
            self._head = node
        
        elif i > self._size:
            if cursor is None:
                cursor = node
            while cursor.getNext() is not None:
                cursor = cursor.getNext()
            cursor.setNext(node)
        else:    
            n = 1
            while n < i -1 and cursor is not None: 
                cursor = cursor.getNext()
                n +=1

            if cursor is None:
                cursor = node
            else:
                node.setNext(cursor.getNext())
                cursor.setNext(node)

    print('Adding # ', self._size, ' element: ', node.getElement())
    self._size += 1  
    
  def insertElt (self, insrtThis, where, insrtHere):
    """Insert element 'insrtThis' before/after node with element =='insrtHere'.
       Parameter 'where' = "B" (before) or "A' (After) 'insrtHere'.        """
    node = self._Node(insrtThis, None)
    # insert method body below
    # Hint: search for the list node element == 'insrtHere', then insert accordingly...' 
    
    if self.isEmpty():
        self._head = node
    else:
        cursor = self._head
        if self.search(insrtHere) == True:
            while cursor:
            #after
                if where == "A":
                    while cursor is not None:
                        if cursor.getElement() == insrtHere:
                            break
                        cursor = cursor.getNext()
                    node.setNext(cursor.getNext())
                    cursor.setNext(node)
                    break
            #Before
                if where == "B":
                    if cursor.getElement() == insrtHere:
                        node.setNext(cursor)
                        cursor.setNext(node)

                    while cursor is not None:
                        if cursor.getNext().getElement() == insrtHere:
                            break
                        cursor = cursor.getNext()
                    node.setNext(cursor.getNext())
                    cursor.setNext(node)                
                    break
                else:
                    print("Invalid operator")      
        else:
            print("Name not if list\nAdding to Tail")
            if cursor is None:
                cursor = node
            while cursor.getNext() is not None:
                cursor = cursor.getNext()
            cursor.setNext(node)

    
    print('Adding # ', self._size, ' element: ', node.getElement())
    self._size += 1
    
    

class Empty(Exception):
    """Empty exception class provided to flag that condition. """
    pass
    
SLL2 = SinglyLinkedList()
nlist= []
fname = '38271878.txt'
f = open (fname)
pFile = f.readlines()
for items in pFile:
    item = items.split(',')

    if len(item)==1:
        item[0] = item[0][:-1]
        nlist.append(item)
        
    if len(item) == 2:
        item[1] = item[1][:-1]
        nlist.append(item)
    
    if len(item) == 3:
        item[2] = item[2][:-1]
        nlist.append(item)
    
    if len(item) == 4:
        item[3] = item[3][:-1]
        nlist.append(item)
    
    else:
        pass

for item in nlist:
    if item[0] == 'A':
        SLL2.add(item[1])
    elif item[0] == 'IA':
        SLL2.insertAfter(int(item[1]),item[2])
    elif item[0] == 'IE':
        SLL2.insertElt(item[1],item[2],item[3])
    elif item[0] == 'R':
        SLL2.remove()
    else:
        pass
print('------------------------------------------------------------------')
print('Showlist|\n---------')
SLL2.showList() 
