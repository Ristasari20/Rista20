from models.parkir import Parkir

def main():
    parkir = Parkir()

    # Memulai proses parkir
    parkir.mulai_parkir("Rista", "2024-06-08 08:00", "Mobil")
    parkir.mulai_parkir("Sari", "2024-06-08 09:00", "Motor")

    # Mengakhiri proses parkir
    parkir.akhir_parkir("Rista", "2024-06-08 12:00")
    parkir.akhir_parkir("Sari", "2024-06-08 10:00")

    # Menghitung dan menampilkan biaya parkir
    parkir.hitung_biaya("Rista")
    parkir.hitung_biaya("Sari")

if __name__ == "__main__":
    main()
