# Error handling == mekanisme untuk mengatasi error yang muncul saat program dijalankan

# def pembagian(angka1, angka2):
#     return angka1 / angka2
# print(pembagian(5, 0))  # ZeroDivisionError
# print(pembagian(5, "2"))  # TypeError

# Cara menangani error
def pembagian(angka1, angka2):
    try:
        return angka1 / angka2
    except ZeroDivisionError:
        return "Maaf, tidak bisa dibagi dengan nilai 0"
    except TypeError:
        return "Maaf, tidak bisa menggunakan tipe data ini"
    else:
        return "Kamu memiliki kesalahan pada saat kalkulasi atau blok kode anda"
        # Error selain ZeroDivisionError dan TypeError
    finally:  # selalu dieksekusi dalam kondisi apapun
        return "Program selesai"


print(pembagian(5, 0))
print(pembagian(5, "2"))
