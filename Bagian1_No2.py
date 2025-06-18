angka_list = []
print("Masukkan 10 angka bilangan bulat:")

for i in range(10):
    angka = int(input(f"Bilangan ke-{i + 1}: "))
    angka_list.append(angka)

nilai_minimum = min(angka_list)
nilai_maksimum = max(angka_list)

print(f"\nList bilangan: {angka_list}")
print(f"Nilai minimum: {nilai_minimum}")
print(f"Nilai maksimum: {nilai_maksimum}")
