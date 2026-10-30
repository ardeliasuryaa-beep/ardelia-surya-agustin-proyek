import os

def tampilkan_dan_simpan_laporan(hasil, nama_file_output="output/laporan.txt"):
    if not hasil:
        print("[Peringatan] Tidak ada data valid yang dapat diproses.")
        return

    laporan = f"""
========================================
   LAPORAN REKAP DAN ANALISIS NILAI
========================================
Total Siswa       : {hasil['total_siswa']}
Rata-rata Kelas   : {hasil['rata_rata']:.2f}
Nilai Minimum     : {hasil['minimum']}
Nilai Maksimum    : {hasil['maksimum']}
Siswa Tuntas      : {hasil['jumlah_lulus']}
Siswa Belum Tuntas: {hasil['jumlah_belum_lulus']}
========================================
"""
    print(laporan)
    
    os.makedirs(os.path.dirname(nama_file_output), exist_ok=True)
    with open(nama_file_output, 'w') as f:
        f.write(laporan)
    print(f"Laporan berhasil disimpan ke {nama_file_output}")