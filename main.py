from task_list import TaskList
from task import Task

def main():
    todo = TaskList()
    todo.load_file()

    while True:
        print(f'\n ----ToDo APP----')
        print(f'1. Показать список')
        print(f'2. Добавить задачу')
        print(f'3. Отметить задачу выполненной')
        print(f'4. Сохранить и выйти')

        choice = input("Выберите действие: ")

        if choice == '1':
            for i, task in enumerate(todo.tasks):
                print(i + 1, task)

        elif choice == '2':
            text = input("Введите задачу: ")
            todo.add_task(Task(text))

        elif choice == '3':
            num = int(input("Номер задачи: "))
            todo.tasks[num - 1].completed = True

        elif choice == '4':
            todo.save_file()
            print("До скорой встречи!")
            break

if __name__ == "__main__":
    main()




