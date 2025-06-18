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

    def insert_at(self, position, value):
        if position <= 0:
            nodebaru = Node(value)
            nodebaru.next = self.head
            self.head = nodebaru
            return
        
        node_sekarang = self.head
        count = 0
        while node_sekarang and count < position - 1:
            node_sekarang = node_sekarang.next
            count += 1
        
        if not node_sekarang:
            print("Posisi lebih besar dari panjang linked list!")
            return
        
        nodebaru = Node(value)
        nodebaru.next = node_sekarang.next
        node_sekarang.next = nodebaru

    def display(self):
        nodesekarang = self.head
        while nodesekarang:
            print(nodesekarang.data, end='->')
            nodesekarang = nodesekarang.next
        print('None')       

linkedlist = LinkedList()
linkedlist.append('a')
linkedlist.append('b')
linkedlist.append('c')  
print('Linked List Awal :')
linkedlist.display()               

linkedlist.delete_first()
print('\nLinked List Setelah Node Pertama Dihapus :')
linkedlist.display()

linkedlist.append('d')
linkedlist.append('e')
print('\nLinked List Setelah Ditambah Beberapa Node Diakhir :')
linkedlist.display()

linkedlist.insert_at(2, '50')  # Menambahkan '50' pada posisi 2
print('\nLinked List Setelah Menambahkan Node pada Posisi ke-2 :')
linkedlist.display()

linkedlist.insert_at(10, 'X')  # Posisi ini lebih besar dari panjang list