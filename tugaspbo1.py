class Mahasiswa():
    def __init__(self, nama, umur, jurusan):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan
    def get_info(self):
        print(f" Nama        : {self.nama} ")
        print(f" Umur        : {self.umur} ")
        print(f" Jurusan     : {self.jurusan} ")

    def set_nama(self, nama_baru):
        self.nama = nama_baru

    def set_umur(self, umur_baru):
        self.umur = umur_baru


mahasiswa1 = Mahasiswa("Lia", 19, "Pendidikan Teknik Informatika")
mahasiswa2 = Mahasiswa("Hesti", 18, "Pendidikan Teknik Informatika")
mahasiswa3 = Mahasiswa("Syamsa", 19, "Pendidikan Teknik Informatika")
    

mahasiswa1.set_nama("Ayu")
mahasiswa1.set_umur("20")
mahasiswa1.get_info()
print()
mahasiswa2.set_nama("Puspita")
mahasiswa2.set_umur("30")
mahasiswa2.get_info()
print()
mahasiswa3.set_nama("Khaula")
mahasiswa3.set_umur("40")
mahasiswa3.get_info()
print()

