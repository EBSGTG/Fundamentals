import datetime, menu, db
import json

counter = 0


def increment_counter():
    global counter
    counter += 1
    return counter


def recursive_summa_checker():
    try:
        summa_func = float(input("Введіть суму транзакції: "))
    except:
        # if not isinstance(summa_func, float):
        print("Ви ввели неправильно")
        menu.mini_menu()
        choice = int(input())
        if choice == 1:
            menu.menu()
        elif choice == 2:
            recursive_summa_checker()
        elif choice == 3:
            exit()
        else:
            print("Оберіть 1 - 3 для продовження роботи")
            recursive_summa_checker()
    finally:

        return summa_func


def recursive_category_checker():
    categories = ["Їжа", 'Транспорт', 'Розваги', "Відпочинок", "Саморозвиток"]
    for c in range(len(categories)):
        print(f"{c} - {categories[c]}")
    choice = int(input(f"Введіть категорію транзакції: (Від 0 до {len(categories) - 1}): "))
    if 0 <= choice < len(categories):
        category_func = categories[choice]
        return category_func
    else:
        print("Ваш вибір неправильний!")
        menu.mini_menu()
        choice = int(input())
        if choice == 1:
            menu.menu()
        elif choice == 2:
            recursive_category_checker()
        elif choice == 3:
            exit()
        else:
            print("Оберіть 1 - 3 для продовження роботи")
            recursive_category_checker()


def recursive_checker():
    description_func = input(f"Введіть опис транзакції (Він не може бути пустим та бути менше чим 5 символів): ")
    if len(description_func) < 5:
        print("Ваш опис не підходить під умову:")
        menu.mini_menu()
        choice = int(input())
        if choice == 1:
            menu.menu()
        elif choice == 2:
            recursive_checker()
        elif choice == 3:
            exit()
        else:
            print("Оберіть 1 - 3 для продовження роботи")
            recursive_checker()
    return description_func


class Transaction:
    def __init__(self, tid, t_time, description, category, summa):
        self.tid = tid
        self.t_time = t_time
        self.description = description
        self.category = category
        self.summa = summa

    def __str__(self):
        return f"ID: {self.tid}, TIME: {self.t_time}, DESCRIPTION: {self.description}, CATEGORY: {self.category}, SUM: {self.summa}"


class FinanceManger:
    def __init__(self, transaction_list):
        self.transaction_list = transaction_list

    @staticmethod
    def add_transaction(transaction_list):
        tid = counter
        increment_counter()
        t_time = datetime.datetime.now()
        description = recursive_checker()
        category = recursive_category_checker()
        summa = recursive_summa_checker()
        transaction_list.append(Transaction(tid, t_time, description, category, summa))

    def delete_transaction(self, transaction_list):
        tid = input()
        transaction_list.remove(transaction_list[int(tid)])

    def view_transaction(self, transaction_list):
        if len(transaction_list) == 0:
            print("Транзакцій ще немає")
        else:
            for transaction in transaction_list:
                print(transaction)

    @staticmethod
    def edit_transaction(transaction_list):
        idt = input()
        Transaction = transaction_list[int(idt)]
        Transaction.tid = Transaction.tid
        Transaction.t_time = datetime.datetime.now()
        Transaction.description = recursive_checker()
        Transaction.category = recursive_category_checker()
        Transaction.summa = recursive_summa_checker()
        # Transaction.description = input(f"Введіть опис транзакції ({Transaction.description}): ")
        # Transaction.category = input(f"Введіть категорію транзакції ({Transaction.category}): ")
        # Transaction.summa = input(f"Введіть суму транзакції ({Transaction.summa}):")
        transaction_list[int(idt)] = Transaction

    def write_transactions(self, transaction_list):
        print("Введіть назву файлу для збереження транзакцій:")
        name_of_file = input()
        f = open(f"{name_of_file}.txt", "w")
        for transaction in transaction_list:
            f.write(str(transaction))
        f.close()

    def get_transactions(self):
        print("Введіть назву файлу для збереження транзакцій:")
        name_of_file = input()
        with open(f"{name_of_file}.txt", "r", encoding="utf-8") as file:
            transaction_list = [line.strip() for line in file]

        return transaction_list

    def inserting_db(self, transaction_list):
        for transaction in range(len(transaction_list)):
            Transaction = transaction_list[transaction]
            # db.cursor.execute(f'''Insert into test(id,time,description,category,summa) values ({Transaction.tid},{Transaction.t_time},{Transaction.description}, 1,{Transaction.summa})''')
            insert_query = """
            INSERT INTO test (id, time, description, category, summa)
            VALUES (%s, %s, %s, %s, %s)
            """
            db.cursor.execute(insert_query, (
                Transaction.tid,
                Transaction.t_time,
                Transaction.description,
                Transaction.category,
                Transaction.summa
            ))

    def inserting_to_json(self, transaction_list):
        for x in range(len(transaction_list)):
            y = json.dumps(x.__dict__)
