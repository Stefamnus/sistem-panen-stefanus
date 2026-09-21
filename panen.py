def hitung_total_panen(jumlah_kg, harga_per_kg):
    return jumlah_kg * harga_per_kg


jumlah_panen = 500
harga_per_kg = 7000

total = hitung_total_panen(jumlah_panen, harga_per_kg)

print("Jumlah panen:", jumlah_panen, "kg")
print("Harga per kg: Rp", harga_per_kg)
print("Total hasil panen: Rp", total)
