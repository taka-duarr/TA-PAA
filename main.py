# Fungsi untuk menghitung kebutuhan kalori
def hitung_kalori(berat, tinggi, umur, jenis_kelamin, aktivitas):
    """
    Menghitung kebutuhan kalori harian menggunakan rumus Harris-Benedict
    """
    # Menghitung BMR (Basal Metabolic Rate)
    if jenis_kelamin.lower() == "laki-laki":
        bmr = 88.36 + (13.4 * berat) + (4.8 * tinggi) - (5.7 * umur)
    elif jenis_kelamin.lower() == "perempuan":
        bmr = 447.6 + (9.2 * berat) + (3.1 * tinggi) - (4.3 * umur)
    else:
        raise ValueError("Jenis kelamin harus 'laki-laki' atau 'perempuan'.")

    # Faktor aktivitas
    faktor_aktivitas = {
        "tidak aktif": 1.2,        # Jarang berolahraga
        "ringan": 1.375,           # Aktivitas ringan: 1-3 hari/minggu
        "sedang": 1.55,            # Aktivitas sedang: 3-5 hari/minggu
        "aktif": 1.725,            # Aktif: 6-7 hari/minggu
        "sangat aktif": 1.9        # Sangat aktif: latihan fisik berat
    }

    if aktivitas not in faktor_aktivitas:
        raise ValueError("Tingkat aktivitas tidak valid. Pilih: tidak aktif, ringan, sedang, aktif, atau sangat aktif.")

    # Menghitung total kalori
    kalori = bmr * faktor_aktivitas[aktivitas]
    return round(kalori, 2)


# Fungsi Merge Sort untuk mengurutkan data berdasarkan jumlah kalori
def merge_sort(data):
    if len(data) <= 1:
        return data

    tengah = len(data) // 2
    kiri = merge_sort(data[:tengah])
    kanan = merge_sort(data[tengah:])

    return gabungkan(kiri, kanan)


def gabungkan(kiri, kanan):
    hasil = []
    i = j = 0

    # Menggabungkan dua bagian yang sudah diurutkan
    while i < len(kiri) and j < len(kanan):
        if kiri[i]["kalori"] <= kanan[j]["kalori"]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1

    # Menambahkan sisa data dari kiri
    while i < len(kiri):
        hasil.append(kiri[i])
        i += 1

    # Menambahkan sisa data dari kanan
    while j < len(kanan):
        hasil.append(kanan[j])
        j += 1

    return hasil

def sequential_search(data, nama):
    for pengguna in data:
        if pengguna["nama"].lower() == nama.lower():
            return pengguna
    return None


def hitung_pangkat(basis, pangkat):
    hasil = 1.0  # Mulai dengan nilai 1 (basis^0 = 1)
    
    # Jika pangkat negatif, ubah menjadi positif dan gunakan inversi di akhir
    if pangkat < 0:
        pangkat = -pangkat
        for _ in range(pangkat):
            hasil *= basis
        return 1 / hasil

    # Jika pangkat positif
    for _ in range(pangkat):
        hasil *= basis

    return hasil

def hitung_faktorial(angka):
    if angka < 0:
        return "Faktorial tidak dapat dihitung untuk bilangan negatif."
    elif angka == 0:
        return 1
    else:
        hasil = 1
        for i in range(2, angka + 1):
            hasil *= i
        return hasil

    





# Fungsi utama untuk input dari CLI dengan menu
def main():
    # Data statis
    data_pengguna = [
        {"nama": "Aril", "berat": 60, "tinggi": 170, "umur": 22, "jenis_kelamin": "laki-laki", "aktivitas": "sedang"},
        {"nama": "Mubin", "berat": 55, "tinggi": 160, "umur": 24, "jenis_kelamin": "perempuan", "aktivitas": "ringan"},
        {"nama": "Budi", "berat": 80, "tinggi": 175, "umur": 30, "jenis_kelamin": "laki-laki", "aktivitas": "aktif"},
        {"nama": "Ani", "berat": 50, "tinggi": 155, "umur": 20, "jenis_kelamin": "perempuan", "aktivitas": "tidak aktif"},
        {"nama": "Dika", "berat": 70, "tinggi": 165, "umur": 28, "jenis_kelamin": "laki-laki", "aktivitas": "sangat aktif"},
    ]

    # Menambahkan jumlah kalori ke dalam setiap data pengguna (baik data statis maupun dinamis)
    for pengguna in data_pengguna:
        pengguna["kalori"] = hitung_kalori(pengguna["berat"], pengguna["tinggi"], pengguna["umur"], 
                                            pengguna["jenis_kelamin"], pengguna["aktivitas"])

    while True:
        print("\nMenu:")
        print("1. menghitung kalori anda")
        print("2. Menampilkan semua data yang ada")
        print("3. Mengurutkan data berdasarkan kalori")
        print("4. cari data berdasarkan nama")
        print("5. pangkat umur")
        print("6. Faktorial")
        print("7. Keluar")
        pilihan = input("Pilih menu : ")

        if pilihan == '1':
            # Menghitung jumlah kalori yang dibutuhkan
            print("\nMasukkan data pengguna:")
            nama = input("Nama: ")
            berat = float(input("Berat (kg): "))
            tinggi = float(input("Tinggi (cm): "))
            umur = int(input("Umur: "))
            jenis_kelamin = input("Jenis Kelamin (laki-laki/perempuan): ").lower()
            aktivitas = input("Aktivitas (tidak aktif, ringan, sedang, aktif, sangat aktif): ").lower()

            # Menambahkan data pengguna ke dalam list
            data_pengguna.append({
                "nama": nama,
                "berat": berat,
                "tinggi": tinggi,
                "umur": umur,
                "jenis_kelamin": jenis_kelamin,
                "aktivitas": aktivitas
            })

            # Menambahkan jumlah kalori ke dalam data pengguna
            data_pengguna[-1]["kalori"] = hitung_kalori(berat, tinggi, umur, jenis_kelamin, aktivitas)
            print(f"{nama} - Kalori yang dibutuhkan: {data_pengguna[-1]['kalori']}")

        elif pilihan == '2':
            # Menampilkan semua data yang ada
            if not data_pengguna:
                print("\nTidak ada data pengguna.")
            else:
                print("\nData Pengguna:")
                for pengguna in data_pengguna:
                    print(f" Nama: {pengguna['nama']}")
                    print(f" Berat: {pengguna['berat']}")
                    print(f" Tinggi: {pengguna['tinggi']}")
                    print(f" Umur: {pengguna['umur']}")
                    print(f" Jenis Kelamin: {pengguna['jenis_kelamin']}")
                    print(f" Aktivitas: {pengguna['aktivitas']}")
                    print(f" Kalori: {pengguna['kalori']}")
                    print("-------------------------------------")

        elif pilihan == '3':
            # Mengurutkan data berdasarkan kalori
            if not data_pengguna:
                print("\nTidak ada data untuk diurutkan.")
            else:
                data_terurut = merge_sort(data_pengguna)
                print("\nData Setelah Diurutkan Berdasarkan Kalori:")
                for pengguna in data_terurut:
                    print(f"Nama: {pengguna['nama']}, Kalori yang dibutuhkan: {pengguna['kalori']}")

        elif pilihan == '4':
            # Mencari data berdasarkan nama
            nama = input("\nMasukkan nama yang ingin dicari: ")
            hasil = sequential_search(data_pengguna, nama)
            if hasil:
                print(f"\nData Ditemukan:  \n")
                print("-------------------------------------")
                print(f" Nama: {hasil['nama']}")
                print(f" Berat: {hasil['berat']}")
                print(f" Tinggi: {hasil['tinggi']}")
                print(f" Umur: {hasil['umur']}")
                print(f" Jenis Kelamin: {hasil['jenis_kelamin']}")
                print(f" Aktivitas: {hasil['aktivitas']}")
                print(f" Kalori: {hasil['kalori']}")
                print("-------------------------------------")
            else:
                print("\nData tidak ditemukan.")

        elif pilihan == '5':
            nama = input("\nMasukkan nama pengguna untuk menghitung pangkat umur: ")
            hasil = sequential_search(data_pengguna, nama)
            if hasil:
                iterasi = int(input("\nMasukkan iterasi: "))
                pangkat = hitung_pangkat(hasil['umur'], iterasi)
                print(f"pangkat dari umur {hasil['umur']} untuk {hasil['nama']}: {pangkat}")
            else:
                print("\nData tidak ditemukan.")

        elif pilihan == '6':
            nama = input("\nMasukkan nama pengguna untuk menghitung faktorial: ")
            hasil = sequential_search(data_pengguna, nama)
            if hasil:
                faktorial = hitung_faktorial(hasil['umur'])
                print(f"Faktorial dari {hasil['umur']} untuk {hasil['nama']}: {faktorial}")
            else:
                print("\nData tidak ditemukan.")

        elif pilihan == '7':
            # Keluar dari program
            print("\nTerima kasih telah menggunakan program ini!")
            break

        else:
            print("\nPilihan tidak valid, coba lagi.")


# Menjalankan fungsi utama
# if _name_ == "_main_":
main()  


