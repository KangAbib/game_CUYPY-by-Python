import random

welcome_message = "WELCOME TO CUYPY GAMES!"
cuypy_posisition = random.randint(1,4)

print("***************************")
print(f"**{welcome_message}**")
print("***************************")

nama_user = input("Masukkan Nama Anda: ")

print(f'''
      Halo {nama_user}!
      Perhatikan Goa dibawah ini
      [_] [_] [_] [_]
''')

pilihan_user = int (input("Menurutmu dinomor berapa CUYPY berada ?[1/2/3/4] :"))
# print(f"Pilihanmu adalah {pilihan_user}")


if pilihan_user == cuypy_posisition:
    print(f"Selamat, Anda benar! CUYPY berada di posisisi {cuypy_posisition} dan pilihanmu adalah {pilihan_user}")
else:
    print(f"Maaf, Anda salah! cuypy tidak berada di {pilihan_user} tetapi CUYPY berada di posisi {cuypy_posisition}")
