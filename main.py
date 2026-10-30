from src.input_data import baca_data
from src.proses import analisis_data
from src.output import tampilkan_dan_simpan_laporan

def main():
    print("========================================")
    print("   PROGRAM REKAP DAN ANALISIS NILAI")
    print("========================================")
    
    path_file = "data/contoh_data.txt"
    
    # 1. Membaca dan memvalidasi data dari file
    print(f"Membaca data dari: {path_file} ...")
    data_siswa = baca_data(path_file)
    
    # 2. Memproses statistik dan analisis data
    hasil_analisis = analisis_data(data_siswa)
    
    # 3. Menampilkan ke terminal dan mencetak laporan ke file
    tampilkan_dan_simpan_laporan(hasil_analisis)

if __name__ == "__main__":
    main()