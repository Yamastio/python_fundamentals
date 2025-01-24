# kwargs = keyword arguments
# kwargs adalah sebuah parameter yang bisa diisi dengan sebuah dictionary
# kwargs bisa digunakan untuk menambahkan parameter tambahan ke sebuah fungsi

def pesan_kita(nama: str, **kwargs) -> None:
    pesan = kwargs.get(
        "pesan", "Selamat datang di tutorial python")  # default value
    tinggal = kwargs.get("tinggal")
    print(f"Hello {nama}")
    print(pesan)
    print(f"Saya tinggal di {tinggal}")


# pesan_kita(nama="kyouma")
# pesan_kita(nama="kyouma", pesan="Thank you belajar bahasa python")
pesan_kita(nama="kyouma", pesan="Thank you belajar bahasa python",
           tinggal="Indonesia")
