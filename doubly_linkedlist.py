class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class doublyLL:
    def __init__(self):
        self.head=None

    def print_DLL(self):
        print("")
        if self.head==None:
            print("Linked list is empty to print")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.nref
                
    def print_reverse_DLL(self):
        print("")
        if self.head is None:
            print("Linked list is empty to print in reverse order")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"-->",end="")
                n=n.pref

    def add_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("DLL is not empty")

    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n

    def add_after(self,data,x):
        if self.head is None:
            print("DLL is empty,cannot add after x")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("Element not found,cannot add after")
            else:
                new_node=Node(data)
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node

    def add_before(self,data,x):
        if self.head is None:
            print("DLL is empty,cannot add before x")
        else:
            n=self.head
            while n is not None:
                if x == n.data:
                    break
                n=n.nref
            if n is None:
                print("x not found,cannot add before")
            else:
                new_node=Node(data)
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                n.pref=new_node

    def delete_begin(self):
        if self.head is None:
            print("DLL is empty, no deletion at begin")
            return

        #if only one node present
        if self.head.nref is None:  
            self.head=None
            print("DLL is empty,after deletion at begin")
        else:
            self.head=self.head.nref
            self.head.pref=None

    def delete_end(self):
        if self.head is None:
            print("DLL is empty, no deletion at end")
            return
        
        if self.head.nref is None:
            self.head=None
            print("DLL is empty,after deletion at end")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None

    def delete_by_value(self,x):
        if self.head is None:
            print("DLL is empty, no deletion by value")
            return
        if self.head.nref is None:  #if only one node is present in DLL
            if x==self.head.data:
                self.head=None
            else:
                print("Only one node present,Element not found")
                return
            
        if self.head.data ==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref=n.pref
            n.pref.nref=n.nref
            
        else:  #if it is a last node
            if n.data==x:
                n.pref.nref=None
            else:
                print("Element not found,no deletion by value")
                      
dll=doublyLL()
#dll.add_empty(10) 
#dll.add_empty(20)
dll.add_begin(10)
dll.add_begin(20)
dll.add_begin(30)
dll.add_begin(40)
dll.add_end(50)
dll.add_after(55,20)
dll.add_before(75,30)
dll.print_DLL()

dll.delete_begin()
dll.print_DLL()

dll.delete_by_value(75)
dll.print_DLL()

dll.delete_end()
dll.print_DLL()

dll.print_reverse_DLL()
