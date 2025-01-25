# args = Argument Positional
# args akan menangkap semua argument posisi yang diberikan dan menyimpan dalam bentuk tuple
# menerima data tuple
# args tidak disimpan dalam dictionary, tapi berkerja layaknya tuple yang kosong yang siap diisi
# jika ingin parameter berupa deret nilai maka gunakan args
# jika ingin parameter berupa key, value maka gunakan kwargs


def fungsi_kita(*args) -> None:

    # print dari Argument opsional
    for arg in args:
        print(arg)


fungsi_kita(7, 11, 12, 16, 20)
