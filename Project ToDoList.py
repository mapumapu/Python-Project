model = []


def show_todolist():
    print("TO DO LIST")
    for i in range(0, len(model)):
        todo = model[i]
        no = i + 1

        print(f"{no}. {todo}")


def add_todolist(todo):
    model.append(todo)


def remove_todolist(number):
    del model[number - 1]


def view_show_todolist():
    while True:
        show_todolist()
        print("Menu :")
        print("1 Tambah ")
        print("2 Hapus")
        print("3 Keluar")

        input_user = input("Pilih : ")
        if input_user is "1":
            view_add_todolist()
        elif input_user is "2":
            view_remove_todolist()
        elif input_user is "3":
            break
        else:
            print("Input Salah")


def view_add_todolist():
    print("MENAMBAH TODOLIST")

    input_user = input("Todo (0 jika batal) ")

    if input_user is "0":
        view_show_todolist()
    else:
        add_todolist(input_user)


def view_remove_todolist():
    print("MENGHAPUS TODOLIST")
    
    input_user = int(input("Todo (0 jika batal) "))
    
    if input_user is 0:
        view_show_todolist()
    else:
        remove_todolist(input_user)


view_show_todolist()
    