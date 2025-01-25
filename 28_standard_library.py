# Standard Library = Kumpulan modul yang disediakan oleh Python
# https://docs.python.org/3/library/index.html

import socket
import math
import random

angka_kita: float = 3.14
angka_kita_int: int = 16

print(math.exp(angka_kita))
print(math.sqrt(angka_kita_int))  # akar kuadrat

print(random.randint(1, 10))  # angka acak


# Modul networking

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}, IP Address: {ip_address}")
