from pprint import pprint
import random

# DATASET
kamus = [
    "MATTUJU",
    "PAMMASE",
    "MAPPOJI",
    "RILAPPA",
    "MATTADA",
    "MAPPASA",
    "MAPPAKE",
    "ANREANG",
    "MASEMPO",
    "MATTARO"
]

TARGET = "MAPPADA"

populasi = kamus.copy()

fitness = []
probabilitas = []
interval = []

parent1 = ""
parent2 = ""
child1 = ""
child2 = ""
hasil_mutasi = ""

# FITNESS
def hitung_fitness(kata):
    benar = 0

    for i in range(len(TARGET)):
        if kata[i] == TARGET[i]:
            benar += 1

    return benar / len(TARGET), benar

# MENU 1
def tampil_kamus():
    print("\n=== KAMUS ===")
    for i, k in enumerate(kamus, 1):
        print(i, ".", k)

# MENU 2
def cari_kata():
    kata = input("Masukkan kata : ").upper()

    if kata in kamus:
        print("Kata ditemukan.")
    else:
        print("Kata tidak ditemukan.")

# MENU 3 & 5
def proses_fitness():

    global fitness

    fitness = []

    print("\nHASIL PERHITUNGAN FITNESS")
    print()

    print("{:<4} {:<12} {:<12} {}".format(
        "No",
        "Individu",
        "Huruf Benar",
        "Fitness"
    ))

    print("-" * 42)

    total = 0

    for i, kata in enumerate(populasi, 1):

        f, benar = hitung_fitness(kata)

        fitness.append(f)

        total += f

        print("{:<4} {:<12} {:<12} {:.4f}".format(
            i,
            kata,
            str(benar) + "/7",
            f
        ))

    print("-" * 42)
    print("Total Fitness :", round(total, 4))

    rata = total / len(populasi)

    print("Rata-rata     :", round(rata, 4))

    terbaik = max(fitness)
    indeks = fitness.index(terbaik)

# MENU 6
def roulette():

    global probabilitas
    global interval
    global parent1
    global parent2

    total = sum(fitness)

    probabilitas = []
    interval = []

    kumulatif = 0

    print("\nSELEKSI ROULETTE WHEEL\n")

    print("{:<4} {:<12} {:<10} {}".format(
        "No",
        "Individu",
        "Prob.",
        "Interval"
    ))

    print("-" * 52)

    for i in range(len(populasi)):

        p = fitness[i] / total

        probabilitas.append(p)

        awal = kumulatif
        kumulatif += p

        interval.append((awal, kumulatif))

        print("{:<4} {:<12} {:<10.4f} {:.4f} - {:.4f}".format(
            i + 1,
            populasi[i],
            p,
            awal,
            kumulatif
        ))

    # Bilangan acak
    r1 = random.random()
    r2 = random.random()

    print("\nBilangan Acak")
    print("Random 1 :", round(r1, 4))
    print("Random 2 :", round(r2, 4))

    # Menentukan Parent 1
    for i in range(len(interval)):
        if interval[i][0] <= r1 <= interval[i][1]:
            parent1 = populasi[i]
            break

    # Menentukan Parent 2
    for i in range(len(interval)):
        if interval[i][0] <= r2 <= interval[i][1]:
            parent2 = populasi[i]
            break

    print("\nParent Terpilih")
    print("Parent 1 :", parent1)
    print("Parent 2 :", parent2)

    # Menampilkan fitness parent
    f1, benar1 = hitung_fitness(parent1)
    f2, benar2 = hitung_fitness(parent2)

    print("\nFitness Parent")
    print("{:<10} {:<12} {:<10} {}".format(
        "Parent",
        "Individu",
        "Benar",
        "Fitness"
    ))

    print("-" * 45)

    print("{:<10} {:<12} {:<10} {:.4f}".format(
        "Parent 1",
        parent1,
        str(benar1) + "/7",
        f1
    ))

    print("{:<10} {:<12} {:<10} {:.4f}".format(
        "Parent 2",
        parent2,
        str(benar2) + "/7",
        f2
    ))
    
# MENU 7
def crossover():

    global child1
    global child2
    global target_ditemukan

    if parent1 == "" or parent2 == "":
        print("\nParent belum dipilih.")
        print("Silakan jalankan Menu 6 terlebih dahulu.")
        return

    target_ditemukan = False

    titik = 4

    # Membentuk Child
    child1 = parent1[:titik] + parent2[titik:]
    child2 = parent2[:titik] + parent1[titik:]

    print("\n" + "="*60)
    print("                  PROSES CROSSOVER")
    print("="*60)

    print("Metode           : One Point Crossover")
    print("Titik Potong     : Setelah Gen ke-4")

    print("\nPARENT")

    print("Parent 1")
    print("Kata             :", parent1)
    print("                  {} | {}".format(parent1[:titik], parent1[titik:]))

    print()

    print("Parent 2")
    print("Kata             :", parent2)
    print("                  {} | {}".format(parent2[:titik], parent2[titik:]))

    print("\n" + "-"*60)
    print("PEMBENTUKAN CHILD")
    print("-"*60)

    print("Child 1")
    print("{} + {} = {}".format(
        parent1[:titik],
        parent2[titik:],
        child1
    ))

    print()

    print("Child 2")
    print("{} + {} = {}".format(
        parent2[:titik],
        parent1[titik:],
        child2
    ))

    # Hitung Fitness
    f1, benar1 = hitung_fitness(child1)
    f2, benar2 = hitung_fitness(child2)

    print("\n" + "-"*60)
    print("HASIL CROSSOVER")
    print("-"*60)

    print("{:<10} {:<12} {:<10} {}".format(
        "Child",
        "Individu",
        "Benar",
        "Fitness"
    ))

    print("-"*48)

    print("{:<10} {:<12} {:<10} {:.4f}".format(
        "Child 1",
        child1,
        str(benar1)+"/7",
        f1
    ))

    print("{:<10} {:<12} {:<10} {:.4f}".format(
        "Child 2",
        child2,
        str(benar2)+"/7",
        f2
    ))

    # CEK TARGET
    if child1 == TARGET:

        target_ditemukan = True

        print("\n" + "="*60)
        print("TARGET BERHASIL DITEMUKAN")
        print("="*60)
        print("Target ditemukan pada Child 1.")
        print("Fitness Child 1 : {:.4f}".format(f1))
        print("Mutasi tidak diperlukan karena solusi optimum")
        print("telah diperoleh.")
        print("="*60)

    elif child2 == TARGET:

        target_ditemukan = True

        print("\n" + "="*60)
        print("TARGET BERHASIL DITEMUKAN")
        print("="*60)
        print("Target ditemukan pada Child 2.")
        print("Fitness Child 2 : {:.4f}".format(f2))
        print("Mutasi tidak diperlukan karena solusi optimum")
        print("telah diperoleh.")
        print("="*60)

    else:

        print("\nTarget belum ditemukan.")
        print("Proses dilanjutkan ke tahap mutasi.")
    
# MENU 8
def mutasi():

    global hasil_mutasi
    global target_ditemukan

    if child2 == "":
        print("\nChild belum terbentuk.")
        print("Silakan jalankan Menu 7 terlebih dahulu.")
        return

    print("\n" + "="*60)
    print("                    PROSES MUTASI")
    print("="*60)

    # CEK APAKAH TARGET SUDAH DITEMUKAN
    if target_ditemukan:

        if child1 == TARGET:
            hasil_mutasi = child1
        else:
            hasil_mutasi = child2

        fitness_target, benar_target = hitung_fitness(hasil_mutasi)

        print("Target           :", TARGET)
        print("Individu         :", hasil_mutasi)
        print("Huruf Benar      : {}/7".format(benar_target))
        print("Fitness          : {:.4f}".format(fitness_target))

        print("\n" + "-"*60)
        print("STATUS")
        print("-"*60)
        print("FITNESS SUDAH MENCAPAI 1.0000")
        print("TARGET TELAH DITEMUKAN")
        print("MUTASI TIDAK DILAKUKAN")
        print("Karena solusi optimum telah diperoleh.")

        print("\nHASIL AKHIR")
        print("Individu         :", hasil_mutasi)
        print("Huruf Benar      : {}/7".format(benar_target))
        print("Fitness          : {:.4f}".format(fitness_target))
        print("Status           : TARGET BERHASIL DITEMUKAN")

        print("="*60)

        return

    # PROSES MUTASI
    hasil_mutasi = list(child2)

    print("Target           :", TARGET)
    print("Child Sebelum    :", child2)

    posisi_salah = []

    for i in range(len(TARGET)):
        if hasil_mutasi[i] != TARGET[i]:
            posisi_salah.append(i)

    # Jika ternyata semua gen sudah benar
    if len(posisi_salah) == 0:

        hasil_mutasi = "".join(hasil_mutasi)

        f, benar = hitung_fitness(hasil_mutasi)

        print("\nTidak terjadi mutasi.")
        print("Semua gen sudah sama dengan TARGET.")

        print("\nHasil")
        print("Individu         :", hasil_mutasi)
        print("Huruf Benar      : {}/7".format(benar))
        print("Fitness          : {:.4f}".format(f))
        print("Status           : TARGET BERHASIL DITEMUKAN")

        print("="*60)

        return

    # Memilih salah satu gen yang salah
    posisi = random.choice(posisi_salah)

    huruf_lama = hasil_mutasi[posisi]
    huruf_baru = TARGET[posisi]

    sebelum = "".join(hasil_mutasi)

    hasil_mutasi[posisi] = huruf_baru

    hasil_mutasi = "".join(hasil_mutasi)

    f, benar = hitung_fitness(hasil_mutasi)

    print("\n" + "-"*60)
    print("GEN YANG DIMUTASI")
    print("-"*60)

    print("Posisi Gen       :", posisi + 1)
    print("Huruf Lama       :", huruf_lama)
    print("Huruf Baru       :", huruf_baru)

    print("\nPerubahan Gen")

    print("Sebelum          :", sebelum)
    print("                   " + " " * posisi + "^")

    print("Sesudah          :", hasil_mutasi)
    print("                   " + " " * posisi + "^")

    print("\n" + "-"*60)
    print("HASIL MUTASI")
    print("-"*60)

    print("Huruf Benar      : {}/7".format(benar))
    print("Fitness          : {:.4f}".format(f))

    if hasil_mutasi == TARGET:
        print("Status           : TARGET BERHASIL DITEMUKAN")
    else:
        print("Status           : TARGET BELUM DITEMUKAN")

    print("="*60)
    
# MENU 9
def generasi():

    if child1 == "" or hasil_mutasi == "":
        print("\nGenerasi baru belum dapat dibentuk.")
        print("Silakan jalankan Menu 8 terlebih dahulu.")
        return

    # Hitung fitness kedua individu
    f1, benar1 = hitung_fitness(child1)
    f2, benar2 = hitung_fitness(hasil_mutasi)

    print("\nGENERASI BARU\n")

    print("{:<4} {:<12} {:<12} {}".format(
        "No",
        "Individu",
        "Huruf Benar",
        "Fitness"
    ))
    print("-" * 42)

    print("{:<4} {:<12} {:<12} {:.4f}".format(
        1,
        child1,
        str(benar1) + "/7",
        f1
    ))

    print("{:<4} {:<12} {:<12} {:.4f}".format(
        2,
        hasil_mutasi,
        str(benar2) + "/7",
        f2
    ))

    # Menentukan individu terbaik
    if f1 >= f2:
        terbaik = child1
        fitness_terbaik = f1
        benar_terbaik = benar1
    else:
        terbaik = hasil_mutasi
        fitness_terbaik = f2
        benar_terbaik = benar2

    print("\nIndividu Terbaik")
    print("Kata         :", terbaik)
    print("Huruf Benar  :", str(benar_terbaik) + "/7")
    print("Fitness      :", round(fitness_terbaik, 4))

    if terbaik == TARGET:
        print("Status       : TARGET BERHASIL DITEMUKAN")
    else:
        print("Status       : TARGET BELUM DITEMUKAN")
        print("Generasi berikutnya menggunakan individu terbaik.")

# MENU
while True:

    print("\n" + "="*60)
    print("          PROGRAM ALGORITMA GENETIKA")
    print("     PENCARIAN KATA BAHASA DAERAH BUGIS")
    print("="*60)

    print("1. Tampilkan Kamus")
    print("2. Cari Kata")
    print("3. Jalankan Algoritma Genetika (Fitness)")
    print("4. Tampilkan Populasi")
    print("5. Hasil Fitness")
    print("6. Seleksi Roulette Wheel")
    print("7. Crossover")
    print("8. Mutasi")
    print("9. Generasi Baru")
    print("10. Keluar")

    print("="*60)

    pilih = input("Pilih Menu : ")

    if pilih == "1":
        tampil_kamus()

    elif pilih == "2":
        cari_kata()

    elif pilih == "3":

        print("\n" + "="*60)
        print("        PROSES ALGORITMA GENETIKA DIMULAI")
        print("="*60)

        proses_fitness()

    elif pilih == "4":

        print("\n" + "="*60)
        print("                DATA POPULASI")
        print("="*60)

        print("{:<5}{}".format("No", "Kata"))
        print("-"*60)

        for i, p in enumerate(populasi, 1):
            print("{:<5}{}".format(i, p))

        print("="*60)

    elif pilih == "5":

        proses_fitness()

    elif pilih == "6":

        if len(fitness) == 0:
            print("\nFitness belum dihitung.")
            print("Menghitung fitness terlebih dahulu...\n")
            proses_fitness()

        roulette()

    elif pilih == "7":

        if parent1 == "" or parent2 == "":
            print("\nParent belum tersedia.")
            print("Silakan jalankan Menu 6 terlebih dahulu.")
        else:
            crossover()

    elif pilih == "8":

        if child2 == "":
            print("\nChild belum terbentuk.")
            print("Silakan jalankan Menu 7 terlebih dahulu.")
        else:
            mutasi()

    elif pilih == "9":

        if hasil_mutasi == "":
            print("\nGenerasi baru belum dapat dibuat.")
            print("Silakan jalankan Menu 8 terlebih dahulu.")
        else:
            generasi()

    elif pilih == "10":

        print("\n" + "="*60)
        print("        TERIMA KASIH TELAH MENGGUNAKAN PROGRAM")
        print("="*60)
        print("Program selesai.")
        print("="*60)

        break

    else:

        print("\nPilihan menu tidak tersedia.")
        print("Silakan pilih menu 1 - 10.")