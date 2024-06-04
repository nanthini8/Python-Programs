class Node:  #to create node
    def __init__(self,data):
        self.data=data
        self.ref=None

node1=Node(10)
print(node1)


class LinkedList:
    def __init__(self):
        self.head=None

    #to traverse
    def print_linkedlist(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end='')
                n=n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head == None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x == n.data:
                break
            else:
                n=n.ref
        if n is None:
            print('Element is not present,cannot add node after the element')
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def add_before(self,data,x):
        if self.head.data == x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return  # come out of the function
        if self.head is None:
            print('Linked list is empty, cannot add element at before')
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data ==x:
                break
            n=n.ref
        if n.ref is None:
            print('Element is not present, cannot add node at before')
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def delete_begin(self):
        if self.head is None:
            print('Linked list is empty,No deletion at begin')
        else:
            self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
             print('Linked list is empty,No deletion at end')
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

    def delete_by_value(self,x):
        if self.head is None:
            print('Linked list is empty,no deletion by value')
            return
        if x ==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
        if n.ref is None:
            print('Element not found,no deletion by value')
        else:
            n.ref=n.ref.ref
        
ll=LinkedList()
ll.add_begin(10)
ll.add_begin(20)
ll.add_begin(30)
ll.add_end(40)
ll.add_after(55,20)
ll.add_before(63,40)
ll.print_linkedlist()
print("\n")
ll.delete_begin()
ll.print_linkedlist()
print("\n")
ll.delete_end()
ll.print_linkedlist()
print("\n")
ll.delete_by_value(55)
ll.print_linkedlist()

                
        
        
