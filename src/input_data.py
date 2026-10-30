def baca_data(nama_file):
    data_siswa = []
    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                baris = baris.strip()
                if baris:
                    parts = baris.split(',')
                    if len(parts) == 2:
                        nama = parts[0].strip()
                        try:
                            nilai = float(parts[1].strip())
                            # Validasi rentang nilai 0 - 100
                            if 0 <= nilai <= 100:
                                data_siswa.append({"nama": nama, "nilai": nilai})
                            else:
                                print(f"[Peringatan] Nilai {nilai} untuk {nama} di luar rentang valid (0-100).")
                        except ValueError:
                            print(f"[Peringatan] Format nilai salah untuk data: {baris}")
    except FileNotFoundError:
        print(f"[Error] File {nama_file} tidak ditemukan.")
    return data_siswa