# Mengimpor fungsi dari masing-masing modul
from tambah import tambah
from kurang import kurang
from kali import kali
from bagi import bagi

def main():
    print("="*30)
    print("   KALKULATOR SEDERHANA")
    print("="*30)
    print("Pilih Operasi:")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("5. Keluar")
    print("="*30)

    while True:
        pilihan = input("\nMasukkan pilihan (1/2/3/4/5): ")

        # Cek jika user ingin keluar dari program
        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator ini. Sampai jumpa!")
            break

        # Cek apakah pilihan valid (1-4)
        if pilihan in ('1', '2', '3', '4'):
            try:
                # Meminta input angka dari user dan mengubahnya jadi tipe data float (desimal)
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
            except ValueError:
                # Menangkap error jika user memasukkan huruf/karakter selain angka
                print("Error: Masukkan angka yang valid!")
                continue

            # Menjalankan fungsi sesuai pilihan user
            if pilihan == '1':
                print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")

            elif pilihan == '2':
                print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")

            elif pilihan == '3':
                print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")

            elif pilihan == '4':
                # Mencegah error pembagian dengan angka 0
                if angka2 == 0:
                    print("Error: Tidak bisa membagi angka dengan nol!")
                else:
                    print(f"Hasil: {angka1} / {angka2} = {bagi(angka1, angka2)}")
        else:
            print("Pilihan tidak valid. Silakan pilih angka 1 sampai 5.")

# Memastikan fungsi main() hanya dijalankan jika file ini dieksekusi langsung
if __name__ == "__main__":
    main()
