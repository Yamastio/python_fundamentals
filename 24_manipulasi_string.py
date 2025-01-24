nama_saya = "kyouma"
nama_saya_besar = "KYOUMA"
deskripsi_saya = "saya adalah seorang programmer python"

# uppercase = merubah ke huruf kapital
print(nama_saya.upper())  # KYOUMA

# lowercase = merubah ke huruf kecil
print(nama_saya_besar.lower())  # kyouma

# Replace = mengganti kata tertentu
mengganti_kata = deskripsi_saya.replace("saya", "kamu")
print(mengganti_kata)  # kamu adalah seorang programmer python

# rstrip = menghapus spasi sebelah kanan
kata_saya = " indonesia raya "
print(kata_saya.lstrip())  # indonesia raya

# lstrip = menghapus spasi sebelah kiri
print(kata_saya.rstrip())  # indonesia raya

# strip = menghapus spasi sebelah kiri dan kanan
print(kata_saya.strip())  # indonesia raya

# startswith = mengecek apakah kata dimulai dengan kata yang ditentukan
print(kata_saya.startswith(" in"))  # True

# endswith = mengecek apakah kata diakhiri dengan kata yang ditentukan
print(kata_saya.endswith("raya "))  # True

# title = mengubah kata ke huruf kapital di awal kata
print(kata_saya.title())  # Indonesia Raya

# isdigit = mengecek angka pada sebuah string
umur_saya = "18"
print(umur_saya.isdigit())  # True

# split = memcah kata string menjadi list
print(deskripsi_saya.split())
# ["saya", "adalah", seorang", programmer",  "python"]
