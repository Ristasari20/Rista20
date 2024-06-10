from abc import ABC, abstractmethod

class ParkirAble(ABC):
    @abstractmethod
    def mulai_parkir(self, nama_pengguna, waktu_mulai, jenis_kendaraan):
        pass

    @abstractmethod
    def akhir_parkir(self, nama_pengguna, waktu_akhir):
        pass

    @abstractmethod
    def hitung_biay_parkir(self, nama_pengguna):
        pass
