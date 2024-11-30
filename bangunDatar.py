import math
import time

def hitung_bangun_datar():
    start_time = time.time()
    
    while True:
        print("Pilih Bangun Datar:")
        print("1. Panjang 'Persegi Panjang'")
        print("2. Lebar 'Persegi Panjang'")
        print("3. Persegi")
        print("4. Lingkaran")

        pilihan = int(input("Masukkan pilihan Anda (1-4): "))

        if pilihan == 1:
            print("\nAnda memilih mencari Panjang Persegi Panjang.")
            lebar = float(input("Masukkan Lebar Persegi Panjang: "))
            luas = float(input("Masukkan Luas Persegi Panjang (0 jika tidak ada): "))
            keliling = float(input("Masukkan Keliling Persegi Panjang (0 jika tidak ada): "))

            if luas > 0:
                panjang = luas / lebar
            elif keliling > 0:
                panjang = (keliling / 2) - lebar
            else:
                print("Data tidak valid.")
                continue

            print(f"Diketahui:\nPanjang: {panjang}")

        elif pilihan == 2:
            print("\nAnda memilih mencari Lebar Persegi Panjang.")
            panjang = float(input("Masukkan Panjang Persegi Panjang: "))
            luas = float(input("Masukkan Luas Persegi Panjang (0 jika tidak ada): "))
            keliling = float(input("Masukkan Keliling Persegi Panjang (0 jika tidak ada): "))

            if luas > 0:
                lebar = luas / panjang
            elif keliling > 0:
                lebar = (keliling / 2) - panjang
            else:
                print("Data tidak valid.")
                continue

            print(f"Diketahui:\nLebar: {lebar}")

        elif pilihan == 3:
            print("\nAnda memilih Persegi.")
            luas = float(input("Masukkan Luas Persegi (0 jika tidak ada): "))
            keliling = float(input("Masukkan Keliling Persegi (0 jika tidak ada): "))

            if luas > 0:
                sisi = math.sqrt(luas)
                keliling = 4 * sisi
            elif keliling > 0:
                sisi = keliling / 4
                luas = sisi ** 2
            else:
                print("Data tidak valid.")
                continue

            print(f"Diketahui:\nLuas: {luas}\nKeliling: {keliling}\nSisi: {sisi}")

        elif pilihan == 4:
            print("\nAnda memilih Lingkaran.")
            luas = float(input("Masukkan Luas Lingkaran (0 jika tidak ada): "))
            keliling = float(input("Masukkan Keliling Lingkaran (0 jika tidak ada): "))

            if luas > 0:
                radius = math.sqrt(luas / math.pi)
                keliling = 2 * math.pi * radius
            elif keliling > 0:
                radius = keliling / (2 * math.pi)
                luas = math.pi * radius ** 2
            else:
                print("Data tidak valid.")
                continue

            print(f"Diketahui:\nLuas: {luas}\nKeliling: {keliling}\nRadius: {radius}")

        else:
            print("Pilihan tidak valid.")
            continue

        ulang = input("Ingin mengulang program? (y/n): ").lower()
        if ulang != 'y':
            break

    end_time = time.time()
    runtime = end_time - start_time
    print(f"Waktu eksekusi: {runtime:.2f} detik.")

hitung_bangun_datar()
