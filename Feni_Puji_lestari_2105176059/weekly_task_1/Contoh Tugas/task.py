class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def display_info(self):
        print("Informasi Mahasiswa:")
        print(f"Nama: {self.nama}")
        print(f"Kelas: {self.kelas}")
        print(f"Prodi: {self.prodi}")
        print(f"Fakultas: {self.fakultas}")
        print(f"Tempat Tinggal: {self.tempat_tinggal}")
        print(f"Asal: {self.asal}")

# Contoh penggunaan
mahasiswa1 = Mahasiswa("Feni Puji Lestari", "2021 B", "Pendidikan Komputer", "FKIP", "Swandi", "long ikis")
mahasiswa1.display_info()


