# Type casting = mengubah tipe data dari variable

angka = 3.14

# 1. Type casting ke int()
angka_int = int(angka)

print(angka_int)
print(type(angka_int))

# 2. Type casting ke string()
angka_string = str(angka)

print(angka_string)
print(type(angka_string))

# 3. Type casting ke float()
angka_float = float(angka)

print(angka_float)
print(type(angka_float))

# 4. Type casting ke boolean()
angka_boolean = bool(0) # 0 = False, 1 = True

print(angka_boolean)
print(type(angka_boolean))


# String ke float / integer == error
nilai_int= int("3") # 3
# nilai_int = int("empat belas") # ValueError
nilai_float = float("3.14") # 3.14
# nilai_float = float("tiga koma empat belas") # ValueError


# String ke boolean
nilai1 = bool("True") # True
nilai1 = bool("False") # True
nilai1 = bool("0") # True
nilai1 = bool("") # False, jika kosong baru false
