class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class singlylinkedlist:
    def __init__(self):
            self.first=None
    def insertfirst(self,data):
        temp=Node(data)
        temp.next=self.first
        self.first=temp
    def removefirst(self):
        if(self.first==None):
            print("list is empty")
        else:
            cur=self.first
            self.first=self.first.next
            print("the deleted item is",cur.data)
    def display(self):
        if(self.first==None):
            print("list is empty")
            return
        cur=self.first
        while(cur):
            print(cur.data,end=" ")
            cur=cur.next
    def search(self,item):
        if(self.first==None):
            print("list is empty")
            return
        cur=self.first
        while cur!=None:
            if cur.data==item:
                print("item is present in the linked list")
                return
            else:
                cur=cur.next
            print("item is not present in the linked list")
s11=singlylinkedlist()
while(True):
    ch=int(input("\nenter your choice 1-insert 2-delete 3-search 4-display 5-exit:"))
    if(ch==1):
        item=input("enter the element to insert:")
        s11.insertfirst(item)
        s11.display()
    elif(ch==2):
        s11.removefirst()
        s11.display()
    elif(ch==3):
        item=input("enter the element to search:")
        s11.search(item)
    elif(ch==4):
        s11.display()
    else:
        break