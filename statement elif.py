nilai = int(input("Masukkan nilai ujian kamu: "))

if nilai >= 90:
    print("Selamat,nilai kamu A")
elif nilai >= 80:
    print("selamat,nilai kamu B")
elif nilai >= 75:
    print("selamat,nilai kamu C")
elif nilai >= 60:
    print("selamat,nilai kamu D")
else:
  print("nilai kamu E (tidak lulus)")