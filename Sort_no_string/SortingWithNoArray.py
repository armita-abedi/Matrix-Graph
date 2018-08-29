class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None
        
# This is a sorted linked list in an ascending order
# Every added item will be placed in its right position in the list
class sortedLinkedList():
    def __init__ (self):
        self.head = None
        
    def add_node(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            
        elif data <= self.head.data:
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            added = False
            while(current.next != None):
                if data <= current.next.data:
                    newNode.next = current.next
                    current.next = newNode
                    added = True
                    break
                current = current.next
            if added == False:
                current.next = newNode
  
# Function to reverse the charachters within a string (e.g "abc" --> "cba")
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
  
# Function to sort characters withing a string in an ascending order and returns the reversed string
# (e.g. "baca" --> "aabc")

def sortString(s):
    str = ""
    size = sum(map(lambda x:1, s))  # the number of characters in the string
    i = 0
    myList = sortedLinkedList()
    while(i < size):
        myList.add_node(s[i])
        i += 1
    current = myList.head
    while(current != None):
        str += current.data
        current = current.next
    return str

  
input = input()    # Input string 
size =  sum(map(lambda x:1, input))  # The number of characters in the input string
i = 0
myList = sortedLinkedList()
while(i < size):
    temp = ''
    while(i < size and input[i] != ','):  # Read in characters until a ',' is seen 
        temp += input[i]
        i += 1
    myList.add_node(temp)  
    i += 1
    