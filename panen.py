def hitung_total_panen(jumlah_kg, harga_per_kg):
    return jumlah_kg * harga_per_kg


def hitung_diskon(total, persentase_diskon):
    return total - (total * persentase_diskon / 100)


jumlah_panen = 500
harga_per_kg = 7000

total = hitung_total_panen(jumlah_panen, harga_per_kg)
total_setelah_diskon = hitung_diskon(total, 10)

print("Jumlah panen:", jumlah_panen, "kg")
print("Harga per kg: Rp", harga_per_kg)
print("Total hasil panen: Rp", total)
print("Total setelah diskon 10%: Rp", total_setelah_diskon)
