import service

comand =''
while comand != '6':
    service.menu()
    print("Выберите команду:")
    comand=input()
    match comand:
        case "1": 
            service.add_note()
        case "2":
            service.show_notes()
        case "3":
            service.show_notes()
            service.edit_note()
        case "4":
            service.show_notes()
            service.del_note()
        case "5":
            service.sort_notes()
        case "6":
            service.exit()
            break
        case _:
            print("Неверная команда")