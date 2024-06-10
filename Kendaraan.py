from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, nama_pengguna, jenis_kendaraan):
        self.nama_pengguna = nama_pengguna
        self.jenis_kendaraan = jenis_kendaraan

    @abstractmethod
    def get_jenis_kendaraan(self):
        pass

class Mobil(Kendaraan):
    def __init__(self, nama_pengguna):
        super().__init__(nama_pengguna, "Mobil")

    def get_jenis_kendaraan(self):
        return self.jenis_kendaraan

class Motor(Kendaraan):
    def __init__(self, nama_pengguna):
        super().__init__(nama_pengguna, "Motor")

    def get_jenis_kendaraan(self):
        return self.jenis_kendaraan

# Contoh penggunaan
mobil = Mobil("Rista")
#motor = Motor("Sari")

print(mobil.get_jenis_kendaraan())  # Output: Mobil
#print(motor.get_jenis_kendaraan())  # Output: Motor
