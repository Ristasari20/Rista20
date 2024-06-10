def hitung_biaya_parkir(jenis_kendaraan, durasi, biaya):
    if (jenis_kendaraan == "Mobil"):
        tarif = biaya  # contoh tarif per jam untuk mobil
    elif (jenis_kendaraan == "Motor"):
        tarif = biaya  # contoh tarif per jam untuk motor
    else:
        raise ValueError("Jenis kendaraan tidak valid")

    return tarif * durasi

jenis_kendaraan = input("Jenis Kendaraan (Mobil/Motor): ")
durasi = float(input("Durasi Parkir (jam): "))
biaya_per_jam = float(input("Biaya per Jam: "))

biaya_total = hitung_biaya_parkir(jenis_kendaraan, durasi, biaya_per_jam)
print(f"Biaya parkir untuk {jenis_kendaraan} dengan durasi {durasi} jam adalah Rp {biaya_total}")

