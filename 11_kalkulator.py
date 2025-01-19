# Membuat kalkulator sederhana

angka_1 = int(input("Masukkan angka pertama: ")) # casting ke integer
angka_2 = int(input("Masukkan angka kedua: "))
operator = input("Pilih operator [+, -, /, *, ^, %]: ")

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"{angka_1} - {angka_2} = {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"{angka_1} / {angka_2} = {hasil}")
elif operator == "^":
    hasil = angka_1 ** angka_2
    print(f"{angka_1} ^ {angka_2} = {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"{angka_1} * {angka_2} = {hasil}")
elif operator == "%":
    hasil = angka_1 % angka_2
    print(f"{angka_1} % {angka_2} = {hasil}")
else:
    print("Operasi tidak diketahui")
