import datetime

model = {}
parking_space = 20


def add_vehicle(vehicle, time_in):

    if len(model) == parking_space:
        print('Parkir Penuh')
    else:
        model[vehicle] = time_in


def view_add_vehicle():
    print("MASUK PARKIR")

    plat_nomor = input("Plat Nomor(x jika batal) : ")
    time_now = datetime.datetime.now()

    if plat_nomor is "x":
        view_main_menu()
    else:
        add_vehicle(plat_nomor, time_now)


def out_vehicle(vehicle, time_out):
    time_in = model.get(vehicle)
    time_diff = time_out - time_in
    time_secs = time_diff.total_seconds()
    time_hrs = time_secs / (60 * 60)

    if time_hrs < 60:
        total_bill = 2000
    else:
        total_bill = time_hrs * 2000

    return total_bill


def view_out_vehicle():
    print("KELUAR PARKIR")

    plat_nomor = input("Plat Nomor : ")
    time_now = datetime.datetime.now()

    if plat_nomor is "x":
        view_main_menu()
    else:
        print(f"Total Biaya Parkir sebesar : Rp. {out_vehicle(plat_nomor, time_now)}")


def view_main_menu():
    while True:
        print("Menu :")
        print("1 Kendaraan Masuk ")
        print("2 Kendaraan Keluar")
        print("3 Keluar")

        input_user = input("Pilih Menu : ")

        if input_user is "1":
            view_add_vehicle()
        elif input_user is "2":
            view_out_vehicle()
        elif input_user is "3":
            break
        else:
            print("Input Salah")


view_main_menu()
