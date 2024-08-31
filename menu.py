import transaction

finance_manager = transaction.FinanceManger([])


def menu():
    print("Choose your option: ")
    print("1 - Додати транзакцію")
    print("2 - Редагувати транзакцію")
    print("3 - Видалити транзакцію")
    print("4 - Переглянути Транзакцію")
    print("5 - Зберегти до Бази даних")
    print("9 - Вийти")
    # print("6 - Зберегти файл")
    choice = int(input())

    if choice == 1:
        finance_manager.add_transaction(finance_manager.transaction_list)
        menu()
    elif choice == 2:
        finance_manager.edit_transaction(finance_manager.transaction_list)
        menu()
    elif choice == 3:
        finance_manager.delete_transaction(finance_manager.transaction_list)
        menu()
    elif choice == 4:
        finance_manager.view_transaction(finance_manager.transaction_list)
        menu()
    elif choice == 5:
        finance_manager.inserting_db(finance_manager.transaction_list)
        print("Check db")
        menu()
    elif choice == 6:
        finance_manager.write_transactions(finance_manager.transaction_list)
        menu()
    elif choice == 7:
        finance_manager.get_transactions()
        menu()
    elif choice == 9:
        exit()

    else:
        print("Від 1 до 5")
        menu()


def mini_menu():
    print("Оберіть що будете робити далі:")
    print("1 - Перейти до меню")
    print("2 - Спробувати ще раз")
    print("3 - Вийти")