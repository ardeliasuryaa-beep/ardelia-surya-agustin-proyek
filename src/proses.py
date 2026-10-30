BATAS_LULUS = 60

def hitung_rata_rata(nilai_list):
    if not nilai_list:
        return 0
    return sum(nilai_list) / len(nilai_list)

def analisis_data(data_siswa):
    if not data_siswa:
        return None
    
    nilai_list = [s['nilai'] for s in data_siswa]
    
    total = len(nilai_list)
    rata_rata = hitung_rata_rata(nilai_list)
    minimum = min(nilai_list)
    maksimum = max(nilai_list)
    
    lulus = [s for s in data_siswa if s['nilai'] >= BATAS_LULUS]
    belum_lulus = [s for s in data_siswa if s['nilai'] < BATAS_LULUS]
    
    return {
        "total_siswa": total,
        "rata_rata": rata_rata,
        "minimum": minimum,
        "maksimum": maksimum,
        "jumlah_lulus": len(lulus),
        "jumlah_belum_lulus": len(belum_lulus)
    }