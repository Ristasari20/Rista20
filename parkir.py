from datetime import datetime

class Parkir:
    def __init__(self):
        self.data_parkir = {}

    def mulai_parkir(self, nama_pengguna, waktu_mulai, jenis_kendaraan):
        self.data_parkir[nama_pengguna] = {
            "waktu_mulai": datetime.strptime(waktu_mulai, "%Y-%m-%d %H:%M"),
            "jenis_kendaraan": jenis_kendaraan,
            "waktu_akhir": None,
            "biaya": 0
        }
        print(f"{nama_pengguna} mulai parkir dengan {jenis_kendaraan} pada {waktu_mulai}")

    def akhir_parkir(self, nama_pengguna, waktu_akhir):
        if nama_pengguna in self.data_parkir:
            self.data_parkir[nama_pengguna]["waktu_akhir"] = datetime.strptime(waktu_akhir, "%Y-%m-%d %H:%M")
            print(f"{nama_pengguna} mengakhiri parkir pada {waktu_akhir}")
        else:
            print(f"{nama_pengguna} tidak ditemukan dalam data parkir.")

    def hitung_biaya(self, nama_pengguna):
        if nama_pengguna in self.data_parkir and self.data_parkir[nama_pengguna]["waktu_akhir"] is not None:
            waktu_mulai = self.data_parkir[nama_pengguna]["waktu_mulai"]
            waktu_akhir = self.data_parkir[nama_pengguna]["waktu_akhir"]
            durasi = (waktu_akhir - waktu_mulai).total_seconds() / 3600  # durasi dalam jam

            # Misalkan biaya parkir per jam adalah 10 untuk Mobil dan 5 untuk Motor
            biaya_per_jam = 10 if self.data_parkir[nama_pengguna]["jenis_kendaraan"] == "Mobil" else 5
            biaya = durasi * biaya_per_jam
            self.data_parkir[nama_pengguna]["biaya"] = biaya
            print(f"Biaya parkir untuk {nama_pengguna} adalah {biaya:.2f} (Durasi: {durasi:.2f} jam)")
        else:
            print(f"Data parkir tidak lengkap untuk {nama_pengguna}.")

def main():
    parkir = Parkir()

    # Memulai proses parkir
    parkir.mulai_parkir("Rista", "2024-06-08 08:00", "Mobil")
    parkir.mulai_parkir("Gilang", "2024-06-08 09:00", "Motor")

    # Mengakhiri proses parkir
    parkir.akhir_parkir("Rista", "2024-06-08 12:00")
    parkir.akhir_parkir("Gilang", "2024-06-08 10:00")

    # Menghitung dan menampilkan biaya parkir
    parkir.hitung_biaya("Rista")
    parkir.hitung_biaya("Gilang")

if __name__ == "__main__":
    main()
