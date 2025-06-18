my_list = []
my_list.extend([10, 20, 30, 40, 50])

print("List sebelum operasi:", my_list)

my_list.pop(0)  # Menghapus elemen pertama
my_list.pop()   # Menghapus elemen terakhir
my_list.insert(2, 25)  # Menyisipkan angka 25 pada indeks ke 2

print("List setelah operasi:", my_list)
