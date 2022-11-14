#****************************************************#
#*   AUTHOR      : hashem_husseen                   *#
#*   Description : Singly Linked Lists              *#
#*   DATE        :   Nov 2022                       *#
#*   VERSION     : V01                              *#
#****************************************************#

#Node of a Singly Linked List 

from hashlib import new
from itertools import count
from select import select


class Node: 
#constructor 
    def __init__(self,data=None): 
        self.data = None
        self.next= None 
#method for setting the data field of the node 
    def setData(self,data):
        self.data=data 

#method for getting the data field of the node 
    def getData(self):
        return self.data 
    
# method for setting the next field of the node 
    def setNext(self,next):
        self.next=next 
 
#method for getting the next field of the node 
    def getNext(self): 
        return self.next
    
    def hasNext(self): 
      return self.next!= None



# A Linked List class with a single head node
class LinkedList:

  def __init__(self):  
    self.head=None
    self.length=0

#method for return the lenght of the linked list 
  def listlengh(self):
    current=self.head
    count=0
    while current!=None:
        count+=1
        current=current.getNext()
    return count 
      

#method for inserting a new node at the beginning of the Linked List (at the head) 
  def insertAtBeginning(self,data): 
    new_node=Node()
    new_node.setData(data)
    if self.length==0 :
      self.head=new_node
    else:
       new_node.setNext(self.head)
       self.head=new_node
       
    self.length+=1




#method for inserting a new node at the end of a Linked List 
  def insertAtEnd(self,data):
    new_node=Node()
    new_node.setData(data)
    current = self.head

    while current.getNext()!=None:
        current=current.getNext()

    current.setNext(new_node) 
    self.length+=1

    




#Method for inserting a new node a t a ny position in a Linked List 
  def insertAtPos(self,pos,data): 
    new_node=Node(data)
    if pos == 0:
       self.insertAtBeginning(data)

    elif pos == self.size :
       self.insertAtEnd(data)
    
    else:
      current = self.head
      count =1
      while count <pos -1 :
        count+=1
        current=current.next
      new_node.next= current.next
      current.next=new_node
      self.size+=1
  
      




#Method for printing all the linkedlist 
  def printList(self): 
    currentNode=self.head 
    if currentNode== None: return 0 
    while currentNode!=None:
      print (currentNode.getData()) 
      currentNode = currentNode.getNext() 









## check creation of list and first insert
l=LinkedList()
l.insertAtBeginning(6)
l.insertAtBeginning(7)
l.insertAtBeginning(8)
l.insertAtEnd(15)
# l.insertAtPos(3,9)
print(l.length)
l.printList()
# Please don't forget to take a screen shot for output.


# ## check node
# n = Node()
# n.setData(5)
# print(n.getData())

# Please don't forget to take a screen shot for output.
