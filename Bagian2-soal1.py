class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
                
    def append(self, data):
        nodebaru = Node(data)
        if self.head == None:
            self.head = nodebaru
            return
        nodeakhir = self.head
        while nodeakhir.next:
            nodeakhir = nodeakhir.next
        nodeakhir.next = nodebaru

    def delete_first(self):
        if self.head == None:
            return
        self.head = self.head.next

    def display(self):
        nodesekarang = self.head
        while nodesekarang:
            print(nodesekarang.data, end='->')
            nodesekarang = nodesekarang.next
        print('None')       

#Tambah data awal
linkedlist = LinkedList()
linkedlist.append('a')
linkedlist.append('b')
linkedlist.append('c')  
print('Linked List Awal :')
linkedlist.display()               

#Delete first
linkedlist.delete_first()
print('\nLinked List Setelah Node Pertama Dihapus :')
linkedlist.display()

#Append akhir
linkedlist.append('d')
linkedlist.append('e')
print('\nLinked List Setelah Ditambah Beberapa Node Diakhir :')
linkedlist.display()