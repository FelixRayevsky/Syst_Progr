
class Task:
    def __init__(self, task_id, operation, filename, content=None, line_num=None, schedule=None):
        self.task_id = task_id
        self.operation = operation
        self.filename = filename
        self.content = content
        self.line_num = line_num
        self.schedule = schedule

    def __repr__(self):
        return f"<Task id={self.task_id}, operation={self.operation}, filename={self.filename}, schedule={self.schedule}>"

class FileOperations:

    @staticmethod
    def create_file(filename, content):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

    @staticmethod
    def append_to_file(filename, content):
        with open(filename, "a", encoding="utf-8") as file:
            file.write(content + "\n")

    @staticmethod
    def delete_file(filename):
        import os
        os.remove(filename)

class Scheduler:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, operation, filename, content=None, line_num=None, schedule=None):
        task = Task(
            self.next_id,
            operation,
            filename,
            content,
            line_num,
            schedule
        )

        self.tasks.append(task)
        self.next_id += 1

        return task
    
    def run_task(self, task):
        if task.operation == "create":
            FileOperations.create_file(task.filename, task.content)

        elif task.operation == "append":
            FileOperations.append_to_file(task.filename, task.content)

        elif task.operation == "delete":
            FileOperations.delete_file(task.filename)

        else:
            print("Неизвестная операция")

##====================================================================================

scheduler = Scheduler()

while True:
    print("\n=== ФАЙЛОВЫЙ ШЕДУЛЕР ===")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Выполнить задачи")
    print("4. Удалить задачу")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        print("\nДобавление задачи")
        print("\n=== ВЫБЕРИТЕ ОПЕРАЦИЮ ===")
        print("1. Создать файл")
        print("2. Дополнить файл")
        print("3. Удалить файл")

        operation_choice = input("Выберите операцию: ")

        if operation_choice == "1":
            print("\nВыбрано: создать файл\n")
            filename = input("Введите имя файла: ")
            content = input("Введите содержимое файла: ")
            operation = "create"

        elif operation_choice == "2":
            print("\nВыбрано: дополнить файл\n")
            filename = input("Введите имя файла: ")
            content = input("Введите содержимое файла: ")
            operation = "append"

        elif operation_choice == "3":
            print("\nВыбрано: удалить файл\n")
            filename = input("Введите имя файла: ")
            operation = "delete"

        else:
            print("Неизвестная операция\n")
            continue




        print("\n=== РАСПИСАНИЕ ===")
        print("1. Без расписания")
        print("2. Каждый день")
        print("3. Каждую неделю")

        schedule_choice = input("Выберите расписание: ")

        if schedule_choice == "1":
            schedule = None

        elif schedule_choice == "2":
            schedule = "daily"

        elif schedule_choice == "3":
            schedule = "weekly"

        else:
            print("Неизвестное расписание")
            schedule = None


        scheduler.add_task(
            operation,
            filename,
            content if operation != "delete" else None,
            schedule = schedule
        )

        print("Задача добавлена!")



    elif choice == "2":
        print("\n=== СПИСОК ЗАДАЧ ===")

        if len(scheduler.tasks) == 0:
            print("Задач пока нет.")
        else:
            for task in scheduler.tasks:
                print(task)
                
    elif choice == "3":
        print("\n=== ВЫПОЛНЕНИЕ ЗАДАЧ ===")

        if len(scheduler.tasks) == 0:
            print("Задач пока нет.")
        else:
            for task in scheduler.tasks:
                print("Выполняется:", task)
                scheduler.run_task(task)

            print("Все задачи выполнены!")

    elif choice == "4":
        print("\n=== УДАЛЕНИЕ ЗАДАЧИ ===")

        if len(scheduler.tasks) == 0:
            print("Задач пока нет.")
        else:
            task_id = int(input("Введите ID задачи: "))

            for task in scheduler.tasks:
                if task.task_id == task_id:
                    scheduler.tasks.remove(task)
                    print("Задача удалена.")
                    break
            else:
                print("Задача с таким ID не найдена.")
    
    elif choice == "0":
        print("Выход из программы")
        break
    else:
        print("Неизвестная команда")

