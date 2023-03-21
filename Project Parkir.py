import datetime, math

daftar_kendaraan = {}
maximum_tempat_parkir = 20


def kendaraan_masuk(kendaraan, waktu_masuk):

    if len(daftar_kendaraan) == maximum_tempat_parkir:
        print('Parkir Penuh')
    else:
        daftar_kendaraan[kendaraan] = waktu_masuk


def tampilan_kendaraan_masuk():
    print("MASUK PARKIR")

    plat_nomor = input("Plat Nomor(x jika batal) : ")
    
    # Untuk input waktu secara real-time
    time_now = datetime.datetime.now()

    # Untuk input waktu secara manual
    time_str = '2023-03-17 01:17:16.436536'
    time_manual = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f')

    if plat_nomor == "x":
        tampilan_menu_utama()
    else:
        # jgn lupa ubah variable time_manual ke time_now kalau ingin pakai waktu yang real-time
        kendaraan_masuk(plat_nomor, time_manual)


def kendaraan_keluar(kendaraan, waktu_keluar):
    waktu_masuk = daftar_kendaraan.get(kendaraan)
    perbedaan_waktu = waktu_keluar - waktu_masuk
    waktu_dalam_jam = perbedaan_waktu.total_seconds() / 3600

    if waktu_dalam_jam < 1:
        total_biaya_parkir = 2000
    else:
        total_biaya_parkir = math.ceil(waktu_dalam_jam) * 2000

    return waktu_masuk, total_biaya_parkir


def tampilan_kendaraan_keluar():
    print("KELUAR PARKIR")

    plat_nomor = input("Plat Nomor : ")
    
    # Untuk input waktu secara real-time
    time_now = datetime.datetime.now()

    # Untuk input waktu secara manual
    time_str = '2023-03-17 05:40:16.436536'
    time_manual = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f')

    if plat_nomor == "x":
        tampilan_menu_utama()
    else:
        # jgn lupa ubah variable time_manual ke time_now kalau ingin pakai waktu yang real-time
        waktu_masuk, total_biaya_parkir = kendaraan_keluar(plat_nomor, time_manual)
        print(f"Plat Nomor : {plat_nomor}")
        print(f"Waktu Masuk : {waktu_masuk}")
        print(f"Waktu Keluar : {time_manual}")
        print(f"Total durasi parkir(jam:menit:detik) : {time_manual - waktu_masuk}")
        print(f"Total Biaya Parkir : Rp. {total_biaya_parkir}")


def tampilan_daftar_kendaraan():
    if len(daftar_kendaraan) == 0:
        print("Tidak ada kendaraan yang diparkir saat ini.")
    else:
        print("Daftar Kendaraan yang Diparkir:")
        for kendaraan in daftar_kendaraan:
            print(f"{kendaraan} ({daftar_kendaraan[kendaraan]})")


def tampilan_menu_utama():
    while True:
        print("Menu :")
        print("1 Kendaraan Masuk ")
        print("2 Kendaraan Keluar")
        print("3 Lihat Daftar Kendaraan")
        print("4 Keluar")

        input_user = input("Pilih Menu : ")

        if input_user == "1":
            tampilan_kendaraan_masuk()
        elif input_user == "2":
            tampilan_kendaraan_keluar()
        elif input_user == "3":
            tampilan_daftar_kendaraan()
        elif input_user == "4":
            break
        else:
            print("Input Salah")


tampilan_menu_utama()

#perlu tambah waktu keluar dan masuk di tampilan kendaraan keluar
#bagusin tampilan outputnya

