print("Data kelulusan Siswa Taman Cadika Mesra")
print(" ")

nama = str(input("Masukan Nama Siswa : "))
nt = float(input("Masukan Nilai Teori Siswa : "))
np = float(input("Masukan Nilai Praktek Siswa : "))

if nt >= 70 <= np:
    print("Selamat, Anda LULUS!")
elif np <= 70 <= nt:
    print("Anda harus mengulang ujian praktek.")
elif nt <= 70 <= np:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")