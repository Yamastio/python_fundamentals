angka_saya = 10
angka_kamu = 5
hasil = angka_saya + angka_kamu


def tambah(angka1: int, angka2: int) -> int:
    try:
        if angka1 < - 0:
            return "tidak boleh dibawah nol"
        if angka2 < 0:
            return "tidak boleh dibawah nol"
        return angka1 + angka2
    except TypeError:
        return "Tipe data salah, harusnya integer"


def kurang(angka1: int, angka2: int) -> int:
    try:
        if angka1 < - 0:
            return "tidak boleh dibawah nol"
        if angka2 < 0:
            return "tidak boleh dibawah nol"
        return angka1 - angka2
    except TypeError:
        return "Tipe data salah, harusnya integer"
